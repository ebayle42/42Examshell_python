import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_palindrome_partitioner.py")
r = t.rng
cases = ["aab", "aba", "abc", "", "a", "aa", "ab", "racecar", "abcd", "aabbaa", "banana",
         "noonabbad", "ababbbabbababa", "abcdefgh", "aaaaaaaaaaaaaaaaaaaab"]
cases += ["".join(r.choice("abc") for _ in range(r.randint(0, 16))) for _ in range(300)]
cases.append("".join(r.choice("ab") for _ in range(400)))
t.func("palindrome_partitioner", cases).done()
