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
cases += [[], ["1"], ["2", "1"], ["1", "1", "1"], ["3", "1", "2", "1", "3"]]
cases += [[str(r.randint(-50, 50)) for _ in range(r.randint(1, 30))] for _ in range(100)]
t.cases(cases).done()
