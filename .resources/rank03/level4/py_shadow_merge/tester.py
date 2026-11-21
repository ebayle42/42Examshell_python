import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_shadow_merge.py")
r = t.rng
cases = [([1, 3, 5], [2, 4, 6]), ([1, 2, 3], [4, 5, 6]), ([1], [2, 3, 4]), ([], [1, 2, 3]),
         ([1, 1, 2], [1, 3, 3]), ([], []), ([4, 5], []), ([-3, 0], [-5, 7])]
for _ in range(300):
    a = [r.randint(-20, 20) for _ in range(r.randint(0, 10))]
    b = [r.randint(-20, 20) for _ in range(r.randint(0, 10))]
    a.sort()
    b.sort()
    cases.append((a, b))
t.func("shadow_merge", cases).done()
