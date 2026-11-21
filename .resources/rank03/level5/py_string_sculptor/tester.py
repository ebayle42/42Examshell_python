import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_string_sculptor.py")
r = t.rng
cases = ["hello", "Hello World", "   hello   ", "abc123def", "Python3.9!", "", "A", "123", "a b c d",
         "HELLO WORLD", "42 is the answer"]
cases += ["".join(r.choice("abcXYZ 12.!") for _ in range(r.randint(0, 20))) for _ in range(400)]
t.func("string_sculptor", cases).done()
