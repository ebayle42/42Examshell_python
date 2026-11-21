import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_prism_detector.py")
r = t.rng
cases = [(["CAT", "A..", "T.."], "CAT"), ([], "CAT"), (["CAT"], ""), (["TAC"], "CAT"),
         (["C..", ".A.", "..T"], "CAT"), (["..C", ".A.", "T.."], "CAT"), (["T..", ".A.", "..C"], "CAT"),
         (["ABA", "BAB", "ABA"], "AB"), (["XYZ", "XYZ"], "QQ")]
for _ in range(300):
    h, w = r.randint(1, 6), r.randint(1, 6)
    grid = ["".join(r.choice("ABC") for _ in range(w)) for _ in range(h)]
    pattern = r.choice(["AB", "ABC", "CAB", "BA", "AAB", "ABCA"])
    cases.append((grid, pattern))
# the order of the matches is free: only the set of (x, y, direction) is compared
t.func("prism_detector", cases, unordered=True).done()
