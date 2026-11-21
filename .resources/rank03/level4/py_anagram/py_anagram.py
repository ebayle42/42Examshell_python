def anagram(s1: str, s2: str) -> bool:
    def counts(s):
        d = {}
        for c in s.lower():
            if c != " ":
                d[c] = d.get(c, 0) + 1
        return d

    return counts(s1) == counts(s2)
