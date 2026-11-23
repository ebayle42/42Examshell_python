"""Shared test engine for the Python exam shell.

Each exercise folder contains:
    sub.txt / sub.fr.txt   the subject
    <file>.py              the reference solution
    tester.py              the test cases, built on this module

The student's file is expected at  <repo>/rendu/<exercise>/<file>.py
Every test runs the student's code AND the reference solution on the same
input and compares the results.
"""
from __future__ import annotations

import ast
import contextlib
import copy
import importlib.util
import io
import os
import random
import signal
import sys
import traceback

sys.dont_write_bytecode = True

TIME_LIMIT = 20  # seconds for the whole test run

if sys.stdout.isatty() or os.environ.get("FORCE_COLOR"):
    RED, GREEN, YELLOW, CYAN, BOLD, RESET = (
        "\033[31m", "\033[32m", "\033[33m", "\033[36m", "\033[1m", "\033[0m")
else:
    RED = GREEN = YELLOW = CYAN = BOLD = RESET = ""


class _Timeout(Exception):
    pass


def _short(value, limit=300):
    text = repr(value)
    return text if len(text) <= limit else text[:limit] + "..."


def _fmt_args(args):
    return ", ".join(_short(a, 120) for a in args)


def _normalize(value):
    """Treat tuples and lists alike when comparing results."""
    if isinstance(value, (list, tuple)):
        return [_normalize(v) for v in value]
    if isinstance(value, dict):
        return {k: _normalize(v) for k, v in value.items()}
    return value


def _same_type_family(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return isinstance(a, bool) and isinstance(b, bool)
    return True


def equal(expected, got, unordered=False):
    if not _same_type_family(expected, got):
        return False
    e, g = _normalize(expected), _normalize(got)
    if unordered and isinstance(e, list) and isinstance(g, list):
        try:
            return sorted(map(repr, e)) == sorted(map(repr, g))
        except TypeError:
            return False
    return e == g


class Tester:
    def __init__(self, tester_file, filename, forbidden=None, seed=None):
        self.dir = os.path.dirname(os.path.abspath(tester_file))
        self.exercise = os.path.basename(self.dir)
        self.filename = filename
        repo = os.path.abspath(os.path.join(self.dir, "..", "..", "..", ".."))
        self.student_path = os.environ.get(
            "EXAM_STUDENT_FILE",
            os.path.join(repo, "rendu", self.exercise, filename))
        self.ref_path = os.path.join(self.dir, filename)
        self.forbidden = forbidden or []
        self.count = 0
        self.rng = random.Random(seed if seed is not None else 42)
        if hasattr(signal, "SIGALRM"):
            signal.signal(signal.SIGALRM, self._on_timeout)
            signal.alarm(TIME_LIMIT)
        self.ref = self._load(self.ref_path, "reference_solution", is_ref=True)
        self.student = self._load_student()

    # ------------------------------------------------------------------ setup
    @staticmethod
    def _on_timeout(signum, frame):
        raise _Timeout()

    def _load(self, path, modname, is_ref=False):
        spec = importlib.util.spec_from_file_location(modname, path)
        module = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
        return module

    def _load_student(self):
        if not os.path.isfile(self.student_path):
            self.fail(f"File not found: rendu/{self.exercise}/{self.filename}")
        with open(self.student_path, encoding="utf8") as fh:
            source = fh.read()
        if not source.strip():
            self.fail(f"rendu/{self.exercise}/{self.filename} is empty")
        try:
            tree = ast.parse(source)
        except SyntaxError as exc:
            self.fail(f"Syntax error line {exc.lineno}: {exc.msg}")
        self._check_forbidden(tree)
        try:
            return self._load(self.student_path, "student_solution")
        except _Timeout:
            self.timeout()
        except BaseException:
            self.fail("Your file raised an error when imported:\n"
                      + traceback.format_exc(limit=-3))

    def _check_forbidden(self, tree):
        """Rules: 'sorted()' call, '.sort()' method, 'heapq' module,
        'heapq.merge()' / 'collections.OrderedDict' qualified names."""
        calls, methods, modules, qualified = set(), set(), set(), set()
        for rule in self.forbidden:
            rule = rule.strip()
            if rule.endswith("()"):
                rule = rule[:-2]
            if rule.startswith("."):
                methods.add(rule[1:])
            elif "." in rule:
                parts = rule.split(".")
                if parts[0] == "list" and len(parts) == 2:
                    methods.add(parts[1])
                elif parts[0] == "collections" and parts[1] == "deque" and len(parts) == 3:
                    methods.add(parts[2])
                else:
                    qualified.add((".".join(parts[:-1]), parts[-1]))
            elif rule in ("sorted", "eval", "exec", "sum", "max", "min", "reversed"):
                calls.add(rule)
            else:
                modules.add(rule)
        names_from_qualified = {n for _, n in qualified}

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in modules:
                        self.fail(f"Forbidden import: {alias.name} (line {node.lineno})")
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                if mod.split(".")[0] in modules:
                    self.fail(f"Forbidden import: {mod} (line {node.lineno})")
                for alias in node.names:
                    if (mod, alias.name) in qualified:
                        self.fail(f"Forbidden: {mod}.{alias.name} (line {node.lineno})")
            elif isinstance(node, ast.Call):
                func = node.func
                if isinstance(func, ast.Name) and func.id in calls:
                    self.fail(f"Forbidden function: {func.id}() (line {node.lineno})")
                if isinstance(func, ast.Attribute) and func.attr in methods:
                    self.fail(f"Forbidden method: .{func.attr}() (line {node.lineno})")
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and (node.value.id, node.attr) in qualified:
                    self.fail(f"Forbidden: {node.value.id}.{node.attr} (line {node.lineno})")
                # distinctive class names (OrderedDict, TopologicalSorter) via any alias
                if node.attr in names_from_qualified and node.attr[:1].isupper():
                    self.fail(f"Forbidden: {node.attr} (line {node.lineno})")

    # ------------------------------------------------------------- reporting
    def fail(self, message, expected=None, got=None, show=False):
        print(f"{RED}{BOLD}FAIL{RESET}  {message}")
        if show:
            print(f"{GREEN}Expected:{RESET} {_short(expected, 1000)}")
            print(f"{RED}Got:     {RESET} {_short(got, 1000)}")
        sys.exit(1)

    def timeout(self):
        print(f"{RED}{BOLD}TIMEOUT{RESET}  more than {TIME_LIMIT}s "
              "(infinite loop or too slow algorithm?)")
        sys.exit(1)

    def _student_attr(self, name):
        if not hasattr(self.student, name):
            self.fail(f"'{name}' is not defined in {self.filename}")
        return getattr(self.student, name)

    def _call(self, fn, args):
        """Return (ok, value_or_traceback)."""
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                return True, fn(*copy.deepcopy(args))
        except _Timeout:
            self.timeout()
        except RecursionError:
            return False, "RecursionError: maximum recursion depth exceeded"
        except Exception:
            return False, traceback.format_exc(limit=-1).strip().splitlines()[-1]

    # ----------------------------------------------------------------- tests
    def func(self, name, cases, unordered=False, checker=None):
        """Compare student's `name(*args)` with the reference for every case.

        cases: iterable of argument tuples.
        checker(args, expected, got) -> bool  (optional custom validation)
        """
        student_fn = self._student_attr(name)
        ref_fn = getattr(self.ref, name)
        for args in cases:
            if not isinstance(args, tuple):
                args = (args,)
            self.count += 1
            _, expected = self._call(ref_fn, args)
            ok, got = self._call(student_fn, args)
            call = f"{name}({_fmt_args(args)})"
            if not ok:
                self.fail(f"test {self.count}: {call} raised an exception:\n    {got}")
            good = checker(args, expected, got) if checker else equal(expected, got, unordered)
            if not good:
                self.fail(f"test {self.count}: {call}", expected, got, show=True)
        return self

    def ops(self, class_name, scenarios):
        """Run method-call scenarios on the student's class and the reference.

        scenario: (ctor_args, [(method, args), ...])
        Pseudo-method '==find' compares find(a) == find(b) instead of raw roots.
        """
        student_cls = self._student_attr(class_name)
        ref_cls = getattr(self.ref, class_name)
        for ctor_args, steps in scenarios:
            self.count += 1
            trace = [f"obj = {class_name}({_fmt_args(ctor_args)})"]
            ok, ref_obj = self._call(ref_cls, ctor_args)
            ok, obj = self._call(student_cls, ctor_args)
            if not ok:
                self.fail(f"test {self.count}: {trace[0]} raised:\n    {obj}")
            for method, args in steps:
                if method == "==find":
                    trace.append(f"obj.find({args[0]}) == obj.find({args[1]})")
                    e_ok, e = self._call(lambda a, b: ref_obj.find(a) == ref_obj.find(b), args)
                    g_ok, g = self._call(
                        lambda a, b: self._method(obj, "find")(a) == self._method(obj, "find")(b),
                        args)
                else:
                    trace.append(f"obj.{method}({_fmt_args(args)})")
                    e_ok, e = self._call(getattr(ref_obj, method), args)
                    g_ok, g = self._call(self._method(obj, method), args)
                if not g_ok:
                    self.fail(f"test {self.count}:\n    " + "\n    ".join(trace[-12:])
                              + f"\n    raised: {g}")
                if not equal(e, g):
                    shown = trace if len(trace) <= 12 else ["..."] + trace[-11:]
                    self.fail(f"test {self.count}:\n    " + "\n    ".join(shown), e, g, show=True)
        return self

    def _method(self, obj, name):
        if not hasattr(obj, name):
            self.fail(f"method '{name}' is missing")
        return getattr(obj, name)

    def custom(self, cases, fn):
        """fn(student_module, ref_module, case) -> None or (message, expected, got)."""
        for case in cases:
            self.count += 1
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    problem = fn(self.student, self.ref, copy.deepcopy(case))
            except _Timeout:
                self.timeout()
            except Exception:
                problem = (f"{_short(case, 200)} raised:\n    "
                           + traceback.format_exc(limit=-1).strip().splitlines()[-1], None, None)
            if problem:
                msg, e, g = problem
                self.fail(f"test {self.count}: {msg}", e, g, show=e is not None or g is not None)
        return self

    def done(self):
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
        print(f"{GREEN}{BOLD}PASSED{RESET}  {self.count} tests OK 🎉")
        sys.exit(0)
