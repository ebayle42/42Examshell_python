def pack(strs: list[str]) -> str:
    out = ""
    for s in strs:
        out += str(len(s)) + "#" + s
    return out


def unpack(s: str) -> list[str]:
    result = []
    i = 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return result
