import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['padinton', 'paqefwtdjetyiytjneytjoeyjnejeyj'], ['dddf6vewg64f', 'gtwthgdwthdwgefewehgwrekhwjwi'], ['rien', 'cettephrasenecomparerien'], [], ['rien']]
cases += [["", ""], ["abc", ""], ["", "abc"], ["a", "b", "c"]]
cases += [[S("abcdef 12", 0, 15), S("abcdef 12", 0, 15)] for _ in range(150)]
t.cases(cases).done()
