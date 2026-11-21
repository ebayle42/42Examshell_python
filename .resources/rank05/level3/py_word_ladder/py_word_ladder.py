def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    words = set(sentence)
    if end not in words:
        return 0
    letters = set("".join(sentence) + start)
    frontier = [start]
    seen = {start}
    length = 1
    while frontier:
        nxt = []
        for word in frontier:
            if word == end:
                return length
            for i in range(len(word)):
                for c in letters:
                    candidate = word[:i] + c + word[i + 1:]
                    if candidate in words and candidate not in seen:
                        seen.add(candidate)
                        nxt.append(candidate)
        frontier = nxt
        length += 1
    return 0
