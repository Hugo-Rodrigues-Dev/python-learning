class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self._traverse(word)
        return bool(node and node.is_end)

    def starts_with(self, prefix):
        return self._traverse(prefix) is not None

    def delete(self, word):
        def _delete(node, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return not node.children
            char = word[depth]
            child = node.children.get(char)
            if not child or not _delete(child, depth + 1):
                return False
            del node.children[char]
            return not node.children and not node.is_end

        if not self.search(word):
            return False
        _delete(self.root, 0)
        return True

    def autocomplete(self, prefix, limit=None):
        node = self._traverse(prefix)
        if not node:
            return []

        results = []

        def _collect(current, path):
            if limit is not None and len(results) >= limit:
                return
            if current.is_end:
                results.append(prefix + "".join(path))
            for char, child in sorted(current.children.items()):
                path.append(char)
                _collect(child, path)
                path.pop()

        _collect(node, [])
        return results

    def _traverse(self, text):
        node = self.root
        for char in text:
            node = node.children.get(char)
            if not node:
                return None
        return node


if __name__ == "__main__":
    trie = Trie()
    for word in ["cat", "car", "cart", "dog", "dove", "door"]:
        trie.insert(word)

    print("Search for 'car':", trie.search("car"))
    print("Search for 'cab':", trie.search("cab"))
    print("Starts with 'do':", trie.starts_with("do"))
    print("Autocomplete 'ca':", trie.autocomplete("ca"))

    print("Delete 'cart':", trie.delete("cart"))
    print("Autocomplete 'ca' after deletion:", trie.autocomplete("ca"))