def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {}

    for root in graph:
        if color.get(root, WHITE) != WHITE:
            continue
        stack = [(root, iter(graph.get(root, [])))]
        color[root] = GREY
        while stack:
            node, neighbours = stack[-1]
            for nxt in neighbours:
                state = color.get(nxt, WHITE)
                if state == GREY:
                    return True
                if state == WHITE:
                    color[nxt] = GREY
                    stack.append((nxt, iter(graph.get(nxt, []))))
                    break
            else:
                color[node] = BLACK
                stack.pop()
    return False
