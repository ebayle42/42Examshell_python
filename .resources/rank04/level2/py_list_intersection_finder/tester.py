import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_list_intersection_finder.py")
r = t.rng
cases = [([[1, 2, 3], [2, 3, 4], [2, 3, 5]],), ([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]],),
         ([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]],), ([[1, 2, 3], [4, 5, 6]],), ([],),
         ([[1, 2, 3], []],), ([[5]],), ([[]],), ([[3, 3, 3]],), ([[-2, -1, 0], [-1, 0, 1]],)]
for _ in range(300):
    lists = []
    for _ in range(r.randint(1, 5)):
        lists.append(sorted(r.randint(-5, 10) for _ in range(r.randint(0, 12))))
    cases.append((lists,))
t.func("list_intersection_finder", cases).done()
