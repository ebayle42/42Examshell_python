DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36) or not number:
        return "ERROR"
    value = 0
    for c in number.upper():
        d = DIGITS.find(c)
        if d < 0 or d >= from_base:
            return "ERROR"
        value = value * from_base + d
    if value == 0:
        return "0"
    out = ""
    while value:
        out = DIGITS[value % to_base] + out
        value //= to_base
    return out
