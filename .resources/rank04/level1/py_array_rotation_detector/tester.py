import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_array_rotation_detector.py", forbidden=["collections.deque.rotate()"])
r = t.rng
cases = [([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]), ([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]), ([1, 2, 3], [3, 2, 1]),
         ([1, 2], [1, 2, 3]), ([], []), ([1], [1]), ([1], [2]), ([1, 1, 2], [1, 2, 1]),
         ([1, 1, 2], [1, 2, 2]), (["a", "b", "c"], ["c", "a", "b"]), ([1, 2, 3], [1, 2, 3]), ([], [1])]
for _ in range(400):
    a = [r.randint(0, 3) for _ in range(r.randint(0, 8))]
    k = r.randint(0, 10)
    b = a[k % len(a):] + a[:k % len(a)] if a else []
    if r.random() < 0.4 and b:
        b[r.randrange(len(b))] = r.randint(0, 3)
    if r.random() < 0.1:
        b.append(1)
    cases.append((a, b))
t.func("array_rotation_detector", cases).done()
