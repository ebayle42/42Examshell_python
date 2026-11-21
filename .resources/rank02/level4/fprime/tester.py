import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['225225'], ['8333325'], ['9539'], ['804577'], ['42'], ['1'], [], ['42', '21']]
cases += [["1"], ["2"], ["4"], ["97"], ["1024"], ["2147483647"], ["2147483646"], ["1", "2"]]
cases += [[str(r.randint(1, 10**6))] for _ in range(150)]
t.cases(cases).done()
