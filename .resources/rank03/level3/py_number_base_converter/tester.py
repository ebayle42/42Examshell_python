import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_number_base_converter.py")
r = t.rng
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def enc(n, b):
    if n == 0:
        return "0"
    s = ""
    while n:
        s = DIGITS[n % b] + s
        n //= b
    return s


cases = [("1010", 2, 10), ("FF", 16, 10), ("255", 10, 16), ("123", 10, 2), ("Z", 36, 10),
         ("35", 10, 36), ("123", 1, 10), ("G", 16, 10), ("0", 10, 2), ("0", 2, 16),
         ("10", 10, 37), ("10", 0, 10), ("2", 2, 10), ("", 10, 2), ("12 3", 10, 2),
         ("1-1", 10, 2), ("ZZZZ", 36, 2), ("777", 8, 16), ("00101", 2, 10), ("10", 10, 1)]
for _ in range(400):
    fb, tb = r.randint(2, 36), r.randint(2, 36)
    cases.append((enc(r.randint(0, 10 ** 7), fb), fb, tb))
for _ in range(100):
    fb = r.randint(2, 35)
    bad = DIGITS[r.randint(fb, 35)]
    s = list(enc(r.randint(1, 10 ** 5), fb))
    s.insert(r.randint(0, len(s)), bad)
    cases.append(("".join(s), fb, r.randint(2, 36)))
t.func("number_base_converter", cases).done()
