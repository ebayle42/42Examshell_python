import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_echo_validator.py")
r = t.rng
cases = ["racecar", "A man a plan a canal Panama", "race a car", "Was it a car or a cat I saw",
         "hello", "Madam Im Adam", "madam", "Able was I ere I saw Elba", "", "a", "Aa", "ab",
         "No lemon, no melon", "Step on no pets!", "Never odd or even", "abcba x", "x abcba x"]


def pal():
    half = "".join(r.choice("abcAB") for _ in range(r.randint(1, 6)))
    mid = r.choice(["", "c", "Z"])
    s = half + mid + half[::-1]
    out = ""
    for c in s:
        out += (c.upper() if r.random() < 0.3 else c) + (" " if r.random() < 0.2 else "")
    return out


cases += [pal() for _ in range(200)]
cases += ["x" + "".join(r.choice("abAB ,!") for _ in range(r.randint(0, 8))) for _ in range(200)]
t.func("echo_validator", cases).done()
