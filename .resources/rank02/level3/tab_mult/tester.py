import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['9'], ['19'], []]
cases += [["1"], ["10"], ["238609294"]]
cases += [[str(r.randint(1, 238609294))] for _ in range(80)]
t.cases(cases).done()
