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
cases += [["a"], ["a", "a"], ["a", "a", "a", "a"], ["a", "b", "a", "c", "a"], ["x", "a", "b"],
          ["a", "a", "b", "a"], ["b", "a", "b", "b"]]
cases += [[r.choice("ab")] + [r.choice("abc") for _ in range(r.randint(0, 12))] for _ in range(100)]
t.cases(cases).done()
