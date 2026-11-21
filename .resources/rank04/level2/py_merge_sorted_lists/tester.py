import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_merge_sorted_lists.py", forbidden=["sorted()", ".sort()", "heapq.merge()"])
r = t.rng
cases = [([[1, 3, 5], [2, 4, 6]],), ([[1, 5, 9], [2, 3, 8], [4, 6, 7]],), ([[5], [1, 3], [2, 4]],),
         ([[1, 1, 2], [2, 3, 3]],), ([[], [1, 2, 3]],), ([[]],), ([[-5, -1, 0], [-3, 2, 4]],),
         ([[10], [10], [10]],), ([],), ([[], [], []],), ([[1, 2, 3]],)]
for _ in range(300):
    lists = []
    for _ in range(r.randint(0, 7)):
        lst = [r.randint(-30, 30) for _ in range(r.randint(0, 10))]
        lst.sort()
        lists.append(lst)
    cases.append((lists,))
big = []
for _ in range(50):
    lst = [r.randint(-10 ** 6, 10 ** 6) for _ in range(2000)]
    lst.sort()
    big.append(lst)
cases.append((big,))
t.func("merge_sorted_lists", cases).done()
