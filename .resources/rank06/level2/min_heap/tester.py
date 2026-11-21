import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "min_heap.py", forbidden=["heapq"])
r = t.rng
base = [("push", (5,)), ("push", (3,)), ("push", (8,))]
scenarios = [
    ((), base + [("peek", ())]),
    ((), base + [("pop", ())]),
    ((), base + [("pop", ()), ("peek", ())]),
    ((), base + [("size", ())]),
    ((), [("pop", ())]),
    ((), [("peek", ()), ("size", ())]),
    ((), base + [("pop", ()), ("pop", ()), ("pop", ()), ("pop", ()), ("size", ()), ("peek", ())]),
    ((), [("push", (2,)), ("push", (2,)), ("push", (-1,)), ("pop", ()), ("pop", ()), ("pop", ())]),
]
for _ in range(300):
    steps = []
    for _ in range(r.randint(1, 40)):
        x = r.random()
        if x < 0.5:
            steps.append(("push", (r.randint(-50, 50),)))
        elif x < 0.8:
            steps.append(("pop", ()))
        elif x < 0.9:
            steps.append(("peek", ()))
        else:
            steps.append(("size", ()))
    scenarios.append(((), steps))
big = [("push", (r.randint(-10 ** 6, 10 ** 6),)) for _ in range(20000)] + [("pop", ())] * 20001
scenarios.append(((), big))
t.ops("MinHeap", scenarios).done()
