import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_sliding_window_maximum.py")
r = t.rng
cases = [([1, 3, -1, -3, 5, 3, 6, 7], 3), ([1, 2, 3, 4, 5], 2), ([5, 4, 3, 2, 1], 1), ([1, 2, 3], 3),
         ([1, 2, 3], 4), ([], 2), ([1, 2, 3], 0), ([1, 2, 3], -1), ([4, 4, 4], 2), ([-5, -2, -9], 2)]
for _ in range(300):
    nums = [r.randint(-20, 20) for _ in range(r.randint(0, 15))]
    cases.append((nums, r.randint(-1, 17)))
cases.append(([r.randint(-10 ** 6, 10 ** 6) for _ in range(20000)], 500))
t.func("sliding_window_maximum", cases).done()
