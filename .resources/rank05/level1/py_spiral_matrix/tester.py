import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_spiral_matrix.py")
t.func("generate_spiral", [(n,) for n in [3, 1, 2, 4, 5, 6, 7, 10, 15, 30]]).done()
