def bridge_finder(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    timer = [0]
    disc = {}
    low = {}
    bridges = []

    def dfs(u, parent):
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        skipped_parent = False
        for v in graph.get(u, []):
            if v == parent and not skipped_parent:
                skipped_parent = True
                continue
            if v not in disc:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((min(u, v), max(u, v)))
            else:
                low[u] = min(low[u], disc[v])

    for node in graph:
        if node not in disc:
            dfs(node, None)
    return sorted(bridges)
