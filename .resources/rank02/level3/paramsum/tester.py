import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['1', '2', '3', '5', '7', '24'], ['6', '12', '24'], []]
cases += [[], [""], ["a"], ["a", "b"]] + [["x"] * n for n in (9, 10, 11, 99, 100, 123)]
t.cases(cases).done()
