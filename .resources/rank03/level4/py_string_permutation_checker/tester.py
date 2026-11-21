import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_string_permutation_checker.py")
r = t.rng
cases = [("abc", "bca"), ("abc", "def"), ("listen", "silent"), ("hello", "bello"), ("", ""),
         ("a", ""), ("Abc", "abc"), ("a gentleman", "elegant man"), ("a b", "ab "), ("aab", "abb"),
         ("!?", "?!"), ("ab", "abc")]
for _ in range(400):
    s = "".join(r.choice("abAB !.") for _ in range(r.randint(0, 10)))
    lst = list(s)
    r.shuffle(lst)
    o = "".join(lst)
    if r.random() < 0.4 and o:
        i = r.randrange(len(o))
        o = o[:i] + r.choice("abAB !.") + o[i + 1:]
    cases.append((s, o))
t.func("string_permutation_checker", cases).done()
