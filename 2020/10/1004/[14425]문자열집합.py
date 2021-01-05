import sys
sys.stdin = open('14425.txt', 'r')


class Node:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, words):
        node = self.root
        for word in words:
            if word not in node.children:
                node.children[word] = Node()
            node = node.children[word]
        node.word = True

    def search(self, words):
        node = self.root
        for word in words:
            if word not in node.children:
                return 0
            node = node.children[word]
        return 1 if node.word else 0


N, S = map(int, input().split())
trie = Trie()
for _ in range(N):
    trie.add(str(input()))
count = 0
for _ in range(S):
    count += trie.search(str(input()))
print(count)
