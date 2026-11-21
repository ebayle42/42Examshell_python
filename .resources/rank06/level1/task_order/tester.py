import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "task_order.py", forbidden=["graphlib.TopologicalSorter"])
r = t.rng
cases = [(2, [[1, 0]]), (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), (2, [[0, 1], [1, 0]]), (3, []),
         (1, []), (0, []), (1, [[0, 0]]), (3, [[0, 2], [1, 2]]), (5, [[0, 4], [4, 3], [3, 2], [2, 1]])]
for _ in range(300):
    n = r.randint(1, 10)
    perm = list(range(n))
    r.shuffle(perm)
    pairs = set()
    for _ in range(r.randint(0, 2 * n)):
        i, j = r.randrange(n), r.randrange(n)
        if i == j:
            continue
        a, b = (perm[i], perm[j]) if i > j else (perm[j], perm[i])
        if r.random() < 0.08:
            a, b = b, a  # may create a cycle
        pairs.add((a, b))
    cases.append((n, [list(p) for p in pairs]))
t.func("task_order", cases).done()
