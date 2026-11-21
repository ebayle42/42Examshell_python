import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "redundant_link.py")
r = t.rng
cases = [([[1, 2], [1, 3], [2, 3]],), ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],),
         ([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]],), ([[1, 2], [2, 1]],), ([[2, 1], [1, 3], [3, 2]],)]
for _ in range(300):
    n = r.randint(3, 12)
    edges = [[v, r.randint(1, v - 1)] for v in range(2, n + 1)]
    while True:
        u, v = r.sample(range(1, n + 1), 2)
        if [u, v] not in edges and [v, u] not in edges:
            break
    edges.append([u, v])
    r.shuffle(edges)
    edges = [e if r.random() < 0.5 else e[::-1] for e in edges]
    cases.append((edges,))
t.func("redundant_link", cases).done()
