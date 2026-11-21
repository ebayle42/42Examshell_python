import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['42', '10'], ['42', '12'], ['14', '77'], ['17', '3'], []]
cases += [["1", "1"], ["7", "7"], ["1", "1000"], ["2147483647", "2"], ["42"], ["1", "2", "3"]]
cases += [[str(r.randint(1, 10**6)), str(r.randint(1, 10**6))] for _ in range(100)]
cases += [[str(a * k), str(b * k)] for a, b, k in ((r.randint(1, 50), r.randint(1, 50), r.randint(1, 999)) for _ in range(50))]
t.cases(cases).done()
