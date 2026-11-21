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
cases += [[""], ["a"], ["hello world"], ["x" * 3000]]
cases += [[S("abc XYZ!", 0, 80) for _ in range(4)] for _ in range(60)]
t.cases(cases).done()
