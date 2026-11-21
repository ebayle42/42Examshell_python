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
cases += [["", "", "abc", "", "", "abc", "abcdef", "cba", "hello", "l", "hello", "xyz"]]
for _ in range(100):
    cases.append([S("abcde ", 0, 10), S("abcde ", 0, 4), S("ab", 0, 6), S("b", 0, 2)])
t.cases(cases).done()
