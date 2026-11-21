import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "pack_strings.py", forbidden=["json", "pickle", "eval"])
r = t.rng
cases = [["hello", "world"], [], [""], ["42", "exam#net", "level:6"], ["", ""], ["", "a", ""],
         ["#"], ["3#abc"], ["\n", "a\nb", " "], ["0#", "#0", "##", "::"], ["10#x" * 5], ["é", "中文", "🙂"],
         ["a" * 1000, ""]]
alphabet = "ab#:12 ,;|\\\n\"'"
for _ in range(300):
    cases.append(["".join(r.choice(alphabet) for _ in range(r.randint(0, 8)))
                  for _ in range(r.randint(0, 6))])


def roundtrip(student, ref, strs):
    for name in ("pack", "unpack"):
        if not hasattr(student, name):
            return (f"function '{name}' is not defined", None, None)
    packed = student.pack(list(strs))
    if not isinstance(packed, str):
        return (f"pack({strs!r}) must return a str", "a str", packed)
    back = student.unpack(packed)
    if back != strs:
        return (f"unpack(pack({strs!r}))", strs, back)


t.custom(cases, roundtrip).done()
