def cryptic_sorter(strings: list[str]) -> list[str]:
    def key(s):
        vowels = 0
        for c in s:
            if c in "aeiouAEIOU":
                vowels += 1
        return (len(s), s.lower(), vowels)

    result = list(strings)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and key(result[j]) > key(current):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
