import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_mirror_matrix.py")
r = t.rng
cases = [([[1, 2, 3], [4, 5, 6]],), ([[1, 2], [3, 4], [5, 6]],), ([[7]],), ([[1, 2, 3, 4]],),
         ([[-1, -2], [-3, -4]],), ([[0, 0], [1, 1]],)]
for _ in range(200):
    w = r.randint(1, 6)
    cases.append(([[r.randint(-50, 50) for _ in range(w)] for _ in range(r.randint(1, 6))],))

t.func("mirror_matrix", cases)


def not_mutated(student, ref, case):
    m = [[1, 2, 3], [4, 5, 6]]
    student.mirror_matrix(m)
    if m != [[1, 2, 3], [4, 5, 6]]:
        return ("mirror_matrix must return a NEW matrix (input was modified)", [[1, 2, 3], [4, 5, 6]], m)


t.custom([None], not_mutated).done()
