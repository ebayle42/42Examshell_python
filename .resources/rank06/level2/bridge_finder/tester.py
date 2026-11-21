import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "bridge_finder.py")
r = t.rng
cases = [({0: [1, 2], 1: [0, 2], 2: [0, 1]},), ({0: [1], 1: [0, 2], 2: [1]},),
         ({0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]},), ({},), ({0: [1], 1: [0]},),
         ({0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1], 3: [1, 4], 4: [1, 3]},),
         ({0: [], 1: []},), ({0: [1], 1: [0], 2: [3], 3: [2]},),
         ({5: [3], 3: [5, 9], 9: [3]},)]
for _ in range(300):
    n = r.randint(1, 10)
    adj = {i: [] for i in range(n)}
    for _ in range(r.randint(0, 2 * n)):
        u, v = r.sample(range(n), 2) if n > 1 else (0, 0)
        if u != v and v not in adj[u]:
            adj[u].append(v)
            adj[v].append(u)
    cases.append((adj,))
t.func("bridge_finder", cases).done()
