def island_matrix_counter(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    seen = [[False] * cols for _ in range(rows)]
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and not seen[i][j]:
                islands += 1
                stack = [(i, j)]
                seen[i][j] = True
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if 0 <= ny < rows and 0 <= nx < cols and not seen[ny][nx] \
                                and matrix[ny][nx] == "1":
                            seen[ny][nx] = True
                            stack.append((ny, nx))
    return islands
