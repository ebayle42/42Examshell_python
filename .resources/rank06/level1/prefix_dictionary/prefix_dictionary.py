class PrefixDictionary:
    def __init__(self):
        self.root = {}
        self.END = "$end"

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = True

    def _walk(self, text: str):
        node = self.root
        for c in text:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and self.END in node

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None and (prefix != "" or len(self.root) > 0)
