import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_pattern_tracker.py")
r = t.rng
cases = ["123", "12a34", "987654321", "01234567", "abc", "1a2b3c4", "112233", "", "9", "90",
         "0123456789", "89", "1 2", "45 56 67"]
cases += ["".join(r.choice("0123456789a ") for _ in range(r.randint(0, 20))) for _ in range(400)]
t.func("pattern_tracker", cases).done()
