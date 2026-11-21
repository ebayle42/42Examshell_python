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
cases += [["1", "2"], ["0", "0"], ["-42", "42"], ["2147483647", "-2147483648"]]
cases += [[str(r.randint(-10**9, 10**9)) for _ in range(6)] for _ in range(40)]
t.cases(cases).done()
