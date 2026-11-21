def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    deps = {}
    for pkg, requirements in packages.items():
        deps[pkg] = set(d for d in requirements if d in packages)
    order = []
    remaining = dict(deps)
    while remaining:
        ready = sorted(p for p, d in remaining.items() if not d)
        if not ready:
            return []  # circular dependency
        for p in ready:
            order.append(p)
            del remaining[p]
        for d in remaining.values():
            d.difference_update(ready)
    return order
