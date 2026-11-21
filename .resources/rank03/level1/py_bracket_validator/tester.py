import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_bracket_validator.py")
r = t.rng


def valid(depth=0):
    out = ""
    for _ in range(r.randint(0, 3)):
        o, c = r.choice(["()", "[]", "{}"])
        inner = valid(depth + 1) if depth < 3 else ""
        out += r.choice(["", "x", "ab "]) + o + inner + c
    return out


cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "hello(world)", "((())", "",
         "(", ")", "]", "{", "}{", "abc", "([{}])", "([]{}){}[()]", "((((", "))))",
         "[(])", "{[(a+b)*c]-d}", "func(arr[i]) { return; }", "(()", "())", "[]]"]
cases += [valid() for _ in range(150)]
cases += ["".join(r.choice("()[]{}a ") for _ in range(r.randint(1, 14))) for _ in range(300)]
t.func("bracket_validator", cases).done()
