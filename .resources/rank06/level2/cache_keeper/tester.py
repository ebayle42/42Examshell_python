import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "cache_keeper.py", forbidden=["collections.OrderedDict"])
r = t.rng
scenarios = [
    ((2,), [("put", (1, 1)), ("put", (2, 2)), ("get", (1,))]),
    ((2,), [("put", (1, 1)), ("put", (2, 2)), ("put", (3, 3)), ("get", (1,))]),
    ((2,), [("put", (1, 1)), ("put", (2, 2)), ("get", (1,)), ("put", (3, 3)), ("get", (2,))]),
    ((2,), [("put", (1, 1)), ("put", (2, 2)), ("get", (1,)), ("put", (3, 3)), ("get", (1,))]),
    ((1,), [("put", (1, 1)), ("put", (2, 2)), ("get", (1,)), ("get", (2,))]),
    ((2,), [("put", (1, 1)), ("put", (1, 10)), ("put", (2, 2)), ("put", (3, 3)), ("get", (1,)),
            ("get", (2,)), ("get", (3,))]),
    ((2,), [("put", (1, 1)), ("put", (2, 2)), ("put", (1, 5)), ("put", (3, 3)), ("get", (2,)),
            ("get", (1,))]),
    ((3,), [("get", (7,))]),
]
for _ in range(300):
    cap = r.randint(1, 4)
    steps = []
    for _ in range(r.randint(1, 30)):
        k = r.randint(0, 6)
        steps.append(("put", (k, r.randint(0, 99))) if r.random() < 0.5 else ("get", (k,)))
    scenarios.append(((cap,), steps))
big = []
for i in range(30000):
    big.append(("put", (i % 3000, i)) if i % 3 else ("get", ((i * 7) % 3000,)))
scenarios.append(((1000,), big))
t.ops("CacheKeeper", scenarios).done()
