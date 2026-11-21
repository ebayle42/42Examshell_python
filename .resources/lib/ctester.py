"""Test engine for the C exercises (Rank 02).

Exercise folder layout:
    sub.txt        the subject ("Expected files" / "Allowed functions" are read from it)
    ref/           reference solution (.c / .h), as a student would turn it in
    main.c         test harness for function exercises (absent for programs)
    given/         files handed to the student (copied into rendu/ by the shell)
    tester.py      the test cases, built on this module

The student's work is expected in  <repo>/rendu/<exercise>/
Student and reference are compiled the same way, run on the same inputs,
and their outputs are compared.
"""
from __future__ import annotations

import os
import re
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

CC = os.environ.get("CC", "cc")
CFLAGS = ["-Wall", "-Wextra", "-Werror"]
RUN_TIMEOUT = 3  # seconds per run

if sys.stdout.isatty() or os.environ.get("FORCE_COLOR"):
    RED, GREEN, YELLOW, BOLD, DIM, RESET = (
        "\033[31m", "\033[32m", "\033[33m", "\033[1m", "\033[2m", "\033[0m")
else:
    RED = GREEN = YELLOW = BOLD = DIM = RESET = ""

# symbols the compiler may emit by itself
IMPLICIT = {"memset", "memcpy", "memmove", "dyld_stub_binder"}
ALIASES = {"printf": {"puts", "putchar", "vprintf"}}


def cat_e(data: bytes, max_lines=25) -> str:
    text = data.decode(errors="replace")
    lines = text.split("\n")
    out = [line + "$" for line in lines[:-1]]
    if lines[-1]:
        out.append(lines[-1])
    if len(out) > max_lines:
        out = out[:max_lines] + [f"... ({len(out) - max_lines} more lines)"]
    return "\n    ".join(out) if out else "(nothing)"


class CTester:
    def __init__(self, tester_file, program_name=None):
        self.dir = os.path.dirname(os.path.abspath(tester_file))
        self.exercise = os.path.basename(self.dir)
        self.name = program_name or self.exercise
        repo = os.path.abspath(os.path.join(self.dir, "..", "..", "..", ".."))
        self.repo = repo
        self.student_dir = os.environ.get("EXAM_STUDENT_DIR",
                                          os.path.join(repo, "rendu", self.exercise))
        self.harness = os.path.join(self.dir, "main.c")
        if not os.path.isfile(self.harness):
            self.harness = None
        self.given = os.path.join(self.dir, "given")
        self.tmp = tempfile.mkdtemp(prefix="examshell_")
        self.count = 0
        if not shutil.which(CC):
            self.fail(f"C compiler '{CC}' not found: install gcc or clang")
        sub = open(os.path.join(self.dir, "sub.txt"), encoding="utf8").read()
        self.expected_files = self._field(sub, "Expected files")
        self.allowed = self._allowed(self._field(sub, "Allowed functions"))
        self.ref_bin = self._build(os.path.join(self.dir, "ref"), "ref", check=False)
        self.student_bin = self._build_student()

    # ----------------------------------------------------------------- setup
    @staticmethod
    def _field(sub, name):
        m = re.search(rf"^{name}\s*:\s*(.*)$", sub, re.M)
        return m.group(1).strip() if m else ""

    @staticmethod
    def _allowed(text):
        names = {n.strip() for n in text.replace(" ", ",").split(",")}
        names -= {"", "-", "None", "none"}
        for name in list(names):
            names |= ALIASES.get(name, set())
        return names

    def _sources(self, d):
        return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".c"))

    def _compile(self, sources, out, include_dirs):
        cmd = [CC] + CFLAGS + [f"-I{d}" for d in include_dirs if os.path.isdir(d)]
        cmd += sources + ["-o", out]
        return subprocess.run(cmd, capture_output=True, text=True)

    def _build(self, d, label, check=True):
        sources = self._sources(d)
        if self.harness:
            sources.append(self.harness)
        out = os.path.join(self.tmp, label)
        res = self._compile(sources, out, [d, self.given])
        if res.returncode != 0:
            if not check:
                raise SystemExit(f"reference does not compile:\n{res.stderr}")
            stderr = res.stderr.replace(self.student_dir + "/", f"rendu/{self.exercise}/")
            stderr = stderr.replace(self.dir + "/", "")
            errors = "\n    ".join(stderr.strip().splitlines()[:20])
            if self.harness and ("multiple definition of `main'" in res.stderr
                                 or ("duplicate symbol" in res.stderr and "_main" in res.stderr)):
                errors = "your file must not contain a main() for this exercise\n    " + errors
            self.fail(f"compilation failed:\n    {errors}")
        return out

    def _build_student(self):
        d = self.student_dir
        if not os.path.isdir(d):
            self.fail(f"folder not found: rendu/{self.exercise}/")
        for f in [x.strip() for x in self.expected_files.split(",") if x.strip()]:
            if "*" in f:
                ext = f.replace("*", "")
                if ext == ".c" and not any(x.endswith(".c") for x in os.listdir(d)):
                    self.fail(f"no .c file in rendu/{self.exercise}/")
            elif not os.path.isfile(os.path.join(d, f)):
                self.fail(f"file not found: rendu/{self.exercise}/{f}")
        sources = self._sources(d)
        if not sources:
            self.fail(f"no .c file in rendu/{self.exercise}/")
        if all(os.path.getsize(s) == 0 for s in sources):
            self.fail(f"rendu/{self.exercise}/ only contains empty files")
        binary = self._build(d, "student")
        self._check_allowed(sources, d)
        return binary

    def _check_allowed(self, sources, d):
        defined, undefined = set(), set()
        for i, src in enumerate(sources):
            obj = os.path.join(self.tmp, f"obj{i}.o")
            res = subprocess.run([CC] + CFLAGS + [f"-I{d}", f"-I{self.given}", "-c", src, "-o", obj],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                continue
            nm = subprocess.run(["nm", obj], capture_output=True, text=True).stdout
            for line in nm.splitlines():
                parts = line.split()
                if len(parts) < 2:
                    continue
                kind, sym = parts[-2], parts[-1]
                if sys.platform == "darwin" and sym.startswith("_"):
                    sym = sym[1:]
                if kind == "U":
                    undefined.add(sym)
                elif kind.upper() in "TDBSRC":
                    defined.add(sym)
        used = {s for s in undefined - defined
                if not s.startswith("_") and s not in IMPLICIT and not s.startswith("GLOBAL")}
        used = {re.sub(r"^__(\w+)_chk$", r"\1", s) for s in used}
        forbidden = sorted(used - self.allowed)
        if forbidden:
            allowed = ", ".join(sorted(self.allowed)) or "none"
            self.fail(f"forbidden function(s) used: {', '.join(forbidden)}  (allowed: {allowed})")

    # ------------------------------------------------------------- reporting
    def fail(self, message):
        print(f"{RED}{BOLD}FAIL{RESET}  {message}")
        self.cleanup()
        sys.exit(1)

    def cleanup(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self, binary, args, stdin=None):
        try:
            res = subprocess.run([binary] + list(args), capture_output=True, timeout=RUN_TIMEOUT,
                                 input=stdin)
        except subprocess.TimeoutExpired:
            return None, "TIMEOUT (infinite loop?)"
        if res.returncode < 0:
            try:
                name = signal.Signals(-res.returncode).name
            except ValueError:
                name = f"signal {-res.returncode}"
            pretty = {"SIGSEGV": "Segmentation fault", "SIGBUS": "Bus error",
                      "SIGABRT": "Abort (double free / corrupted memory?)"}.get(name, name)
            return res.stdout, f"crashed: {pretty}"
        return res.stdout, None

    def _describe(self, args):
        if self.harness:
            shown = ", ".join(shlex.quote(a) for a in args[:12]) + (" ..." if len(args) > 12 else "")
            return f"test main.c with inputs: {shown or '(none)'}"
        return "$> " + " ".join(["./" + self.name] + [shlex.quote(a) for a in args]) + " | cat -e"

    # ----------------------------------------------------------------- tests
    def cases(self, cases):
        """cases: iterable of argv lists (strings)."""
        for args in cases:
            args = [str(a) for a in args]
            self.count += 1
            expected, err = self._run(self.ref_bin, args)
            if err:
                raise SystemExit(f"reference failed on {args}: {err}")
            got, err = self._run(self.student_bin, args)
            what = self._describe(args)
            if err:
                self.fail(f"test {self.count}: {what}\n      -> {err}")
            if got != expected:
                print(f"{RED}{BOLD}FAIL{RESET}  test {self.count}: {what}")
                if self.harness:
                    print(f"{DIM}(test main: {os.path.relpath(self.harness, self.repo)}){RESET}")
                print(f"{GREEN}Expected:{RESET}\n    {cat_e(expected)}")
                print(f"{RED}Got:{RESET}\n    {cat_e(got)}")
                self.cleanup()
                sys.exit(1)
        return self

    def done(self):
        self.cleanup()
        print(f"{GREEN}{BOLD}PASSED{RESET}  {self.count} tests OK 🎉")
        sys.exit(0)


def rand_str(rng, alphabet, lo, hi):
    return "".join(rng.choice(alphabet) for _ in range(rng.randint(lo, hi)))
