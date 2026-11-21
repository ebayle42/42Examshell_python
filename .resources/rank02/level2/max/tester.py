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
cases += [[], ["5"], ["-5"], ["1", "2", "3"], ["3", "2", "1"], ["-3", "-2", "-1"], ["-2147483648", "2147483647"]]
cases += [[str(r.randint(-1000, 1000)) for _ in range(r.randint(1, 20))] for _ in range(100)]
t.cases(cases).done()
