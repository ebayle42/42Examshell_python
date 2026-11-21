import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "trie_autocomplete.py")
r = t.rng
cases = [(["apple", "app", "apricot", "banana"], "app"), (["apple", "app", "apricot", "banana"], "ban"),
         (["hello", "world", "help", "heap"], "he"), (["test"], "xyz"),
         (["cat", "car", "card", "care"], "car"), ([], "test"), (["a", "ab", "abc"], ""),
         (["b", "a", "b", "a"], ""), (["Apple", "apple", "APP"], "A"), (["dup", "dup", "dupe"], "du"),
         ([""], ""), (["", "x"], "")]
for _ in range(300):
    words = ["".join(r.choice("abcB") for _ in range(r.randint(1, 5))) for _ in range(r.randint(0, 15))]
    prefix = "".join(r.choice("abcB") for _ in range(r.randint(0, 2)))
    cases.append((words, prefix))
t.func("trie_autocomplete", cases).done()
