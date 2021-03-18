class Node:
    def __init__(self):
        self.children = {}
        self.word = False

    def __repr__(self):
        return f'Node({self.word}:{self.children.items()})'


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word


trie = Trie()
trie.add('apple')
trie.add('appeal')
print(trie.search('apple'))
print(trie.search('a'))
