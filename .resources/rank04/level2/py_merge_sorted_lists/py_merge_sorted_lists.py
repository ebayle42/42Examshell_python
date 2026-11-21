def _merge_two(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    parts = [list(lst) for lst in lists if lst]
    if not parts:
        return []
    while len(parts) > 1:
        merged = []
        for i in range(0, len(parts), 2):
            if i + 1 < len(parts):
                merged.append(_merge_two(parts[i], parts[i + 1]))
            else:
                merged.append(parts[i])
        parts = merged
    return parts[0]
