DIRECTIONS = [
    ((1, 0), "H"), ((-1, 0), "H-"),
    ((0, 1), "V"), ((0, -1), "V-"),
    ((1, 1), "D1"), ((-1, -1), "D1-"),
    ((-1, 1), "D2"), ((1, -1), "D2-"),
]


def prism_detector(grid: list[str], pattern: str):
    if not grid or not pattern:
        return []
    found = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for (dx, dy), code in DIRECTIONS:
                ok = True
                for k, char in enumerate(pattern):
                    cx, cy = x + dx * k, y + dy * k
                    if not (0 <= cy < len(grid) and 0 <= cx < len(grid[cy])) or grid[cy][cx] != char:
                        ok = False
                        break
                if ok:
                    found.append((x, y, code))
    return found
