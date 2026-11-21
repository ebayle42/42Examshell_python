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
cases += [["1", "3", "-1", "2", "0", "0", "0", "-3", "5", "5", "-10", "-7", "3", "-2"]]
cases += [[str(r.randint(-30, 30)) for _ in range(8)] for _ in range(60)]
t.cases(cases).done()
