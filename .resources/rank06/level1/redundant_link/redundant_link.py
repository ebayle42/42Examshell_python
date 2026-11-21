def redundant_link(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = []
    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            answer = [u, v]
        else:
            parent[ru] = rv
    return answer
