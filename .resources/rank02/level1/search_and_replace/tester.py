import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['Papache est un sabre', 'a', 'o'], ['zaz', 'art', 'zul'], ['zaz', 'r', 'u'], ['jacob', 'a', 'b', 'c', 'e'], ['ZoZ eT Dovid oiME le METol.', 'o', 'a'], ['wNcOre Un ExEmPle Pas Facilw a Ecrirw ', 'w', 'e']]
cases += [[], ["abc"], ["abc", "a"], ["abc", "a", "b", "c"], ["", "a", "b"], ["aaa", "a", "a"],
          ["abc", "", "x"], ["abc", "b", ""], ["abc", "ab", "x"], ["abc", "a", "xy"]]
cases += [[S("abc A.", 0, 20), r.choice("abcA. "), r.choice("xyz!_")] for _ in range(150)]
t.cases(cases).done()
