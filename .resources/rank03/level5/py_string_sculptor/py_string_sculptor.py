def string_sculptor(text: str) -> str:
    result = ""
    index = 0
    for c in text:
        if c.isalpha():
            result += c.lower() if index % 2 == 0 else c.upper()
            index += 1
        else:
            result += c
    return result
