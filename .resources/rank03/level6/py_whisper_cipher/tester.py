import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_whisper_cipher.py")
r = t.rng
cases = [("hello", 3), ("Hello World!", 1), ("xyz", 3), ("ABC123def", 5), ("", 10), ("abc", -3),
         ("Zz", 1), ("abc", 26), ("abc", 52), ("abc", -27), ("Hello", 0), ("The Quick Brown Fox", 13)]
for _ in range(400):
    s = "".join(r.choice("abxyzABXYZ 1!") for _ in range(r.randint(0, 15)))
    cases.append((s, r.randint(-60, 60)))
t.func("whisper_cipher", cases).done()
