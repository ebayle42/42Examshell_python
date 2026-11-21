import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['here_is_a_snake_case_word'], ['hello_world'], []]
cases += [[""], ["word"], ["a_b"], ["hello_world_again_and_again"]]
for _ in range(150):
    words = [S("abcdez", 1, 6) for _ in range(r.randint(1, 5))]
    cases.append(["_".join(words)])
t.cases(cases).done()
