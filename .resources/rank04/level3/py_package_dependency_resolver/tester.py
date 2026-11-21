import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "lib"))
from pytester import Tester  # noqa: E402

t = Tester(__file__, "py_package_dependency_resolver.py", forbidden=["graphlib.TopologicalSorter"])
r = t.rng


def kahn_fifo(packages):
    """Kahn's algorithm with an alphabetical FIFO queue: the other accepted tie-break."""
    deps = {p: set(d for d in ds if d in packages) for p, ds in packages.items()}
    users = {p: [] for p in packages}
    for p, ds in deps.items():
        for d in ds:
            users[d].append(p)
    queue = sorted(p for p, ds in deps.items() if not ds)
    order = []
    while queue:
        p = queue.pop(0)
        order.append(p)
        freed = []
        for u in users[p]:
            deps[u].discard(p)
            if not deps[u]:
                freed.append(u)
        queue += sorted(freed)
    return order if len(order) == len(packages) else []


cases = [({"app": ["database"], "database": ["driver"], "driver": []},),
         ({"A": [], "B": ["A"], "C": ["A", "B"]},), ({},), ({"X": ["Y"], "Y": ["X"]},),
         ({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]},),
         ({"solo": []},), ({"self": ["self"]},), ({"a": ["ghost"], "b": ["a", "phantom"]},),
         ({"a": [], "b": ["a"], "c": ["b"], "d": ["c"], "x": ["y"], "y": ["x"]},),
         ({"z": [], "y": [], "x": []},)]
names = ["alpha", "beta", "core", "delta", "echo", "fmt", "gui", "http", "io", "json"]
for _ in range(400):
    pk = r.sample(names, r.randint(1, 8))
    graph = {}
    for i, p in enumerate(pk):
        pool = pk[:i] if r.random() < 0.85 else pk
        graph[p] = r.sample(pool, r.randint(0, min(3, len(pool))))
        if r.random() < 0.1:
            graph[p].append("missing_pkg")
    cases.append((graph,))


def checker(args, expected, got):
    return got == expected or got == kahn_fifo(args[0])


t.func("package_dependency_resolver", cases, checker=checker).done()
