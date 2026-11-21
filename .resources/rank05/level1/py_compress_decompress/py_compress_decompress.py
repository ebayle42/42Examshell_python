def compress(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        count = j - i
        result += s[i] + (str(count) if count > 1 else "")
        i = j
    return result


def decompress(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        digits = ""
        while i < len(s) and s[i].isdigit():
            digits += s[i]
            i += 1
        result += char * (int(digits) if digits else 1)
    return result
