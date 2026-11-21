import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = []
cases += [["8", "5", "7", "4", "11111111", "10001001", "10010001", "10110001", "11100001"],
          ["1", "1", "0", "0", "0"], ["3", "1", "1", "0", "010"], ["3", "3", "1", "1", "000", "000", "000"]]
for _ in range(150):
    w, h = r.randint(1, 12), r.randint(1, 8)
    rows = ["".join(r.choice("0011a") for _ in range(w)) for _ in range(h)]
    cases.append([str(w), str(h), str(r.randrange(w)), str(r.randrange(h))] + rows)
t.cases(cases).done()
