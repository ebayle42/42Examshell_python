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
cases += [["0", "5", "5", "0", "0", "0", "1", "1", "4", "6", "6", "4", "7", "13", "12", "18", "100", "75"]]
cases += [[str(r.randint(0, 60000)) for _ in range(10)] for _ in range(40)]
t.cases(cases).done()
