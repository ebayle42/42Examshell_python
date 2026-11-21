import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_anagram.py")
r = t.rng
cases = [("listen", "silent"), ("Triangle", "Integral"), ("Dormitory", "Dirty Room"),
         ("hello", "world"), ("", ""), ("abc", "abcc"), ("a", "A"), ("  ", ""),
         ("Astronomer", "Moon starer"), ("aab", "abb"), ("The eyes", "They see")]
for _ in range(400):
    s = "".join(r.choice("abcAB  ") for _ in range(r.randint(0, 10)))
    lst = list(s)
    r.shuffle(lst)
    o = "".join(c.swapcase() if r.random() < 0.3 else c for c in lst)
    if r.random() < 0.4:
        o += r.choice("abc ")
    cases.append((s, o))
t.func("anagram", cases).done()
