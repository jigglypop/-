class Node:
    def __init__(self):
        self.children = [-1] * 26
        self.valid = False

    def __repr__(self):
        return f'Node({self.valid}:{self.children})'


class Trie:
    trie = []
    root = 0

    def init(self):
        self.trie.append(Node())
        return len(self.trie) - 1

    def __init__(self):
        self.init()
        self.root = self.init()

    def add(self, s):
        return self._add(self.root, s, 0)

    def _add(self, node, s, index):
        if index == len(s):
            self.trie[node].valid = True
            return
        c = ord(s[index].lower()) - ord('a')
        if self.trie[node].children[c] == -1:
            _next = self.init()
            self.trie[node].children[c] = _next
        child = self.trie[node].children[c]
        self._add(child, s, index+1)

    def search(self, s):
        return self._search(self.root, s, 0)

    def _search(self, node, s, index):
        if node == -1:
            return False
        if index == len(s):
            return self.trie[node].valid
        c = ord(s[index].lower()) - ord('a')
        child = self.trie[node].children[c]
        return self._search(child, s, index + 1)


trie = Trie()
trie.add('apple')
trie.add('appeal')
print(trie.search('appea'))
