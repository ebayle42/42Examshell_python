import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_cryptic_sorter.py", forbidden=["sorted()", ".sort()"])
r = t.rng
cases = [
    (["apple", "cat", "banana", "dog", "elephant"],),
    (["aaa", "bbb", "AAA", "BBB"],),
    (["hello", "world", "hi", "test"],),
    ([],),
    ([""],),
    (["b", "a", "B", "A", ""],),
    (["Zeta", "alpha", "Beta", "gamma", "Delta"],),
    (["abc", "ABC", "aBc", "Abc"],),
]


def word():
    return "".join(r.choice("aAbBeEzZ19") for _ in range(r.randint(0, 5)))


cases += [([word() for _ in range(r.randint(0, 12))],) for _ in range(300)]
t.func("cryptic_sorter", cases).done()
