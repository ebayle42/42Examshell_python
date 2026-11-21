import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "union_find_system.py")
r = t.rng
scenarios = [
    ((5,), [("connected", (0, 1))]),
    ((5,), [("union", (0, 1))]),
    ((5,), [("union", (0, 1)), ("connected", (0, 1))]),
    ((5,), [("union", (0, 1)), ("union", (1, 2)), ("connected", (0, 2))]),
    ((5,), [("union", (0, 1)), ("union", (0, 1))]),
    ((3,), [("union", (0, 1)), ("union", (1, 2)), ("==find", (0, 2))]),
    ((1,), [("find", (0,)), ("connected", (0, 0)), ("union", (0, 0))]),
    ((4,), [("find", (3,)), ("find", (0,))]),
]
for _ in range(300):
    n = r.randint(2, 12)
    steps = []
    for _ in range(r.randint(1, 25)):
        op = r.choice(["union", "union", "connected", "==find"])
        steps.append((op, (r.randrange(n), r.randrange(n))))
    scenarios.append(((n,), steps))
big = [("union", (i, i + 1)) for i in range(0, 4999)] + [("connected", (0, 4999)), ("==find", (17, 4321))]
scenarios.append(((5000,), big))
t.ops("UnionFind", scenarios)


def path_compression(student, ref, case):
    uf = student.UnionFind(6)
    for a, b in [(0, 1), (2, 3), (0, 2), (4, 5), (0, 4)]:
        uf.union(a, b)
    root = uf.find(5)
    for x in range(6):
        if uf.find(x) != root:
            return ("after union(0,1) union(2,3) union(0,2) union(4,5) union(0,4) "
                    f"find({x}) should equal find(5)", root, uf.find(x))


t.custom([None], path_compression).done()
