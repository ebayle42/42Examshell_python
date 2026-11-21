import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_island_matrix_counter.py")
r = t.rng
cases = [([["1", "1", "1", "1", "0"], ["1", "1", "1", "0", "0"], ["1", "1", "1", "1", "0"],
           ["0", "0", "0", "0", "0"]],),
         ([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"],
           ["0", "0", "0", "1", "1"]],),
         ([],), ([[]],), ([["0"]],), ([["1"]],), ([["1", "0", "1"], ["0", "1", "0"], ["1", "0", "1"]],)]
for _ in range(300):
    h, w = r.randint(1, 8), r.randint(1, 8)
    cases.append(([[r.choice("01") for _ in range(w)] for _ in range(h)],))
cases.append(([["1"] * 20 for _ in range(20)],))
t.func("island_matrix_counter", cases).done()
