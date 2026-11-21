import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_word_ladder.py")
r = t.rng
cases = [("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
         ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
         ("a", "c", ["a", "b", "c"]), ("hot", "dog", ["hot", "dog"]), ("hot", "dot", ["dot"]),
         ("cold", "warm", ["cord", "card", "ward", "warm", "worm", "word", "wold", "cold"]),
         ("lost", "cost", ["most", "fist", "lost", "cost", "fish"])]
for _ in range(250):
    words = list({"".join(r.choice("abc") for _ in range(3)) for _ in range(r.randint(1, 15))})
    start = "".join(r.choice("abc") for _ in range(3))
    end = r.choice(words)
    if end == start:
        continue
    cases.append((start, end, words))
t.func("word_ladder", cases).done()
