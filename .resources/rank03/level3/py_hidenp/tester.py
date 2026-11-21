import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_hidenp.py")
r = t.rng
cases = [("abc", "a1b2c3"), ("ace", "abcde"), ("aec", "abcde"), ("", "abc"), ("abc", "ab"),
         ("aaaa", "aaa"), ("sing", "subsequence testing"), ("", ""), ("a", ""), ("A", "a"),
         ("fgex.;", "tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"), ("abc", "2altrb53c.sse")]
for _ in range(400):
    big = "".join(r.choice("abcAB 1") for _ in range(r.randint(0, 12)))
    small = "".join(r.choice("abcAB 1") for _ in range(r.randint(0, 5)))
    cases.append((small, big))
t.func("hidenp", cases).done()
