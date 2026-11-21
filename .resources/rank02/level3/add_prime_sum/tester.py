import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['5'], ['7'], []]
cases += [["0"], ["1"], ["2"], ["3"], ["-5"], ["5", "7"], ["100"], ["1000"], ["10000"]]
cases += [[str(r.randint(1, 3000))] for _ in range(100)]
t.cases(cases).done()
