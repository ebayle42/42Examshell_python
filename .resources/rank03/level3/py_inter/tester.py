import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_inter.py")
r = t.rng
cases = [("hello", "world"), ("banana", "band"), ("abcabc", "bc"), ("abc", "xyz"), ("", "abc"),
         ("abc", ""), ("padinton", "paqefwtdjetyiytjneytjoeyjnejeyj"),
         ("ddf6vewg64f", "gtwthgdwthdwfteewhrtag6h4ffdhsd"), ("rien", "cette phrase ne cache rien"),
         ("Aa", "a"), ("  x  ", " ")]
for _ in range(400):
    a = "".join(r.choice("abcdeAB 12") for _ in range(r.randint(0, 12)))
    b = "".join(r.choice("abcdeAB 12") for _ in range(r.randint(0, 12)))
    cases.append((a, b))
t.func("inter", cases).done()
