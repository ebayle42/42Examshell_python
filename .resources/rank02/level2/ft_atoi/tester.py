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
cases += [["0", "42", "-42", "+42", "   12", "\t\n\v\f\r 7", "--1", "+-1", "-+1", "12ab34", "abc", "", "-",
           "2147483647", "-2147483648", " - 1", "0000123", "-0"]]
for _ in range(60):
    cases.append([r.choice(["", " ", "\t", "  \n"]) + r.choice(["", "-", "+"]) + str(r.randint(0, 10**9))
                  + r.choice(["", "x", " 5", "9"]) for _ in range(5)])
t.cases(cases).done()
