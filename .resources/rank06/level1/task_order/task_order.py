import heapq


def task_order(n: int, prereqs: list[list[int]]) -> list[int]:
    indegree = [0] * n
    users = [[] for _ in range(n)]
    for a, b in prereqs:
        users[b].append(a)
        indegree[a] += 1
    ready = [i for i in range(n) if indegree[i] == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        task = heapq.heappop(ready)
        order.append(task)
        for nxt in users[task]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(ready, nxt)
    return order if len(order) == n else []
