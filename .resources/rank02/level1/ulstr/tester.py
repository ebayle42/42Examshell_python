import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [["L'eSPrit nE peUt plUs pRogResSer s'Il staGne et sI peRsIsTent VAnIte et auto-justification."], ["S'enTOuRer dE sECreT eSt uN sIGnE De mAnQuE De coNNaiSSanCe.  "], ["3:21 Ba  tOut  moUn ki Ka di KE m'en Ka fe fot"], []]
cases += [[""], ["a", "b"], ["[`{@azAZ"]]
cases += [[S("abzAYZ 4.!{@[`", 0, 30)] for _ in range(150)]
t.cases(cases).done()
