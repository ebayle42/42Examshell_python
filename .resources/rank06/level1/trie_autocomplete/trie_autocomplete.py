def trie_autocomplete(words: list[str], prefix: str) -> list[str]:
    END = None
    root = {}
    for word in words:
        node = root
        for c in word:
            node = node.setdefault(c, {})
        node[END] = True

    node = root
    for c in prefix:
        if c not in node:
            return []
        node = node[c]

    results = []

    def collect(node, current):
        if END in node:
            results.append(current)
        for c in sorted(k for k in node if k is not END):
            collect(node[c], current + c)

    collect(node, prefix)
    return results
