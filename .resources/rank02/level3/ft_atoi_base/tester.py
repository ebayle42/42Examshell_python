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
DIG = "0123456789abcdef"
cases += [["0", "10", "42", "10", "-42", "10", "ff", "16", "FF", "16", "12fdb3", "16", "12FDB3", "16",
           "-101", "2", "777", "8", "7fffffff", "16", "-80000000", "16", "", "10", "-", "16", "10", "2"]]
for _ in range(80):
    case = []
    for _ in range(5):
        b = r.randint(2, 16)
        n = r.randint(0, 10**6)
        s = ""
        while True:
            s = DIG[n % b] + s
            n //= b
            if n == 0:
                break
        s = "".join(c.upper() if r.random() < 0.3 else c for c in s)
        case += [r.choice(["", "", "-"]) + s, str(b)]
    cases.append(case)
t.cases(cases).done()
