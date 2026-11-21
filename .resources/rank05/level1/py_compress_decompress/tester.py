import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_compress_decompress.py")
r = t.rng


def runs():
    s = ""
    for _ in range(r.randint(0, 6)):
        s += r.choice("abcXY!") * r.choice([1, 1, 2, 3, 9, 10, 12, 25])
    return s


plain = ["aabcccccaaa", "", "a", "abc", "aaaaaaaaaaaa", "aabb", "zzzzzzzzzzzzzzzzzzzzzz"]
plain += [runs() for _ in range(250)]
t.func("compress", plain)
packed = ["a2bc5a3", "", "a", "a12", "abc", "x1y1", "a10b", "z100"]
packed += [t.ref.compress(runs()) for _ in range(250)]
t.func("decompress", packed)


def roundtrip(student, ref, s):
    back = student.decompress(student.compress(s))
    if back != s:
        return (f"decompress(compress({s!r}))", s, back)


t.custom(plain, roundtrip).done()
