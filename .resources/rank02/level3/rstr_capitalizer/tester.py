import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [[], ['a FiRSt LiTTlE TESt'], ['SecONd teST A LITtle BiT   Moar comPLEX', '   But... This iS not THAT COMPLEX', '     Okay, this is the last 1239809147801 but not    the least    t']]
cases += [[""], ["a"], ["A b C"], ["\tx\ty\t"], ["1abc a1bc"]]
cases += [[S("abZY \t1_.,", 0, 25) for _ in range(r.randint(1, 3))] for _ in range(150)]
t.cases(cases).done()
