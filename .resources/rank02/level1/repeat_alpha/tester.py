import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['abc'], ['Alex.'], ['abacadaba 42!'], [], ['']]
cases += [["a", "b"], ["zZ"], ["Hello, World 42!"]]
cases += [[S("abzAYZ 4.!", 0, 15)] for _ in range(150)]
t.cases(cases).done()
