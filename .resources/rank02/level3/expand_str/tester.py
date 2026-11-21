import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [["See? It's easy to print the same thing"], [' this        time it      will     be    more complex  '], ['No S*** Sherlock...', 'nAw S*** ShErLaWQ...'], ['']]
cases += [["   "], ["\t"], ["word"], ["a", "b"]]
cases += [[S("ab Z\t\t   ,.42", 0, 30)] for _ in range(150)]
t.cases(cases).done()
