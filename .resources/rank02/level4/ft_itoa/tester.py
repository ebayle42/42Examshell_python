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
cases += [["0", "1", "-1", "9", "10", "-10", "2147483647", "-2147483648", "100000", "-99999"]]
cases += [[str(r.randint(-2**31, 2**31 - 1)) for _ in range(10)] for _ in range(30)]
t.cases(cases).done()
