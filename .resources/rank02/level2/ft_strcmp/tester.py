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
cases += [["", "", "a", "", "", "a", "abc", "abc", "abc", "abd", "abd", "abc", "ab", "abc", "abc", "ab"]]
for _ in range(80):
    a = S("abc", 0, 5)
    cases.append([a, a if r.random() < 0.3 else S("abc", 0, 5), S("aB", 0, 3), S("aB", 0, 3)])
t.cases(cases).done()
