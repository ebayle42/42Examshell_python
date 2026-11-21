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
cases += [[], [""], ["hello"], ["Hello World!", "", "\t42\n"]]
cases += [[S("abc XYZ\n!", 0, 30) for _ in range(r.randint(1, 4))] for _ in range(80)]
t.cases(cases).done()
