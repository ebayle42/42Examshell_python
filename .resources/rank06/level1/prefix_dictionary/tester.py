import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "prefix_dictionary.py")
r = t.rng
scenarios = [
    ((), [("insert", ("apple",)), ("search", ("apple",))]),
    ((), [("insert", ("apple",)), ("search", ("app",))]),
    ((), [("insert", ("apple",)), ("starts_with", ("app",))]),
    ((), [("insert", ("apple",)), ("insert", ("app",)), ("search", ("app",))]),
    ((), [("search", ("a",)), ("starts_with", ("a",))]),
    ((), [("insert", ("abc",)), ("starts_with", ("abcd",)), ("search", ("abcd",)),
          ("starts_with", ("abc",)), ("search", ("ab",)), ("insert", ("ab",)), ("search", ("ab",))]),
]


def word():
    return "".join(r.choice("abc") for _ in range(r.randint(1, 5)))


for _ in range(300):
    steps = []
    for _ in range(r.randint(1, 20)):
        steps.append((r.choice(["insert", "insert", "search", "starts_with"]), (word(),)))
    scenarios.append(((), steps))
t.ops("PrefixDictionary", scenarios).done()
