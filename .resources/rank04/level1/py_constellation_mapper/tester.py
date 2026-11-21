import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_constellation_mapper.py")
r = t.rng
cases = [([(0, 0), (1, 1), (2, 2)], 3), ([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3), ([], 2),
         ([(0, 0), (0, 0), (1, 1)], 2), ([(0, 0), (5, 5)], 3), ([(1, 0), (1, 1), (1, 2)], 3),
         ([(0, 0)], 1), ([(-1, 0), (0, -1), (0, 3), (3, 0)], 3), ([(0, 4)], 5), ([(4, 0)], 5)]
for _ in range(300):
    dim = r.randint(1, 8)
    stars = [(r.randint(-2, dim + 1), r.randint(-2, dim + 1)) for _ in range(r.randint(0, 15))]
    cases.append((stars, dim))
t.func("constellation_mapper", cases).done()
