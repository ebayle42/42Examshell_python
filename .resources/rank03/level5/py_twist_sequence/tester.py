import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_twist_sequence.py")
r = t.rng
cases = [([1, 2, 3, 4, 5], 2), ([1, 2, 3], 1), ([1, 2, 3, 4], 0), ([1, 2, 3], 5), ([], 3),
         ([7], 100), ([1, 2], 2), ([1, 2, 3, 4, 5, 6], 6), ([], 0)]
for _ in range(400):
    arr = [r.randint(-9, 9) for _ in range(r.randint(0, 10))]
    cases.append((arr, r.randint(0, 25)))
t.func("twist_sequence", cases).done()
