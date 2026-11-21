import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [["You hate people! But I love gatherings. Isn't it ironic?"], ['abcdefghijklm'], ['Wingardium Leviosa'], []]
cases += [["a"], ["a b"], ["a", "b"]]
cases += [[" ".join(S("abcXYZ.!42", 1, 7) for _ in range(r.randint(1, 8)))] for _ in range(150)]
t.cases(cases).done()
