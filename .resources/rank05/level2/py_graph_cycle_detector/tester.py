import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_graph_cycle_detector.py", forbidden=["graphlib.TopologicalSorter"])
r = t.rng
cases = [({0: [1], 1: [2], 2: [0]},), ({0: [1], 1: [2], 2: []},), ({},), ({0: [0]},),
         ({0: [1, 2], 1: [3], 2: [3], 3: []},), ({0: [1], 1: [], 2: [3], 3: [2]},),
         ({0: [], 1: [], 2: []},), ({0: [1], 1: [2], 2: [3], 3: [1]},)]
for _ in range(300):
    n = r.randint(1, 9)
    graph = {}
    for u in range(n):
        if r.random() < 0.8:
            graph[u] = r.sample([v for v in range(n) if v > u], r.randint(0, min(3, n - u - 1)))
        else:
            graph[u] = r.sample(range(n), r.randint(0, min(3, n)))
    cases.append((graph,))
chain = {i: [i + 1] for i in range(500)}
chain[500] = []
cases.append((chain,))
t.func("py_graph_cycle_detector", cases).done()
