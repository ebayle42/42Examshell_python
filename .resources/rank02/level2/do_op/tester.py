import os
import random
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from ctester import CTester, rand_str  # noqa: E402

t = CTester(__file__)
r = random.Random(42)


def S(alphabet, lo, hi):
    return rand_str(r, alphabet, lo, hi)


cases = [['123', '*', '456'], ['9828', '/', '234'], ['1', '+', '-43'], []]
cases += [["1", "+", "1"], ["-5", "-", "-5"], ["7", "%", "3"], ["-7", "%", "3"], ["-7", "/", "2"],
          ["0", "*", "-1"], ["2147483647", "-", "0"], ["1", "2"], ["1", "+", "2", "3"]]
for _ in range(200):
    op = r.choice("+-*/%")
    a = r.randint(-10**4, 10**4)
    b = r.randint(-10**4, 10**4)
    if op in "/%" and b == 0:
        b = 7
    cases.append([str(a), op, str(b)])
t.cases(cases).done()
