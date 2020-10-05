import sys
from collections import deque
sys.stdin = open('9250.txt', 'r')


class Node:
    def __init__(self):
        self.children = [-1] * 26
        self.valid = False


class Trie:
    def init(self):
        x = Node()
        self.trie.append(x)
        return len(self.trie) - 1

    def __init__(self):
        self.trie = []
        self.root = self.init()

    def add(self, node, string, index):
        if index == len(string):
            self.trie[node].valid = True
            return
        c = ord(string[index]) - ord('a')
        if self.trie[node].children[c] == -1:
            next = self.init()
            self.trie[node].children[c] = next
        child = self.trie[node].children[c]
        self.add(child, string, index + 1)

    def search(self, node, string, index):
        if node == -1:
            return False
        if index == len(string):
            return self.trie[node].valid
        c = ord(string[index]) - ord('a')
        child = self.trie[node].children[c]
        return self.search(child, string, index + 1)


_trie = Trie()


n = int(sys.stdin.readline())
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    _trie.add(_trie.root, temp, 0)

node = _trie.root
root = _trie.root
trie = _trie.trie
Q = deque()
trie[root].pi = root
Q.append(root)
while Q:
    cur = Q.popleft()
    for i in range(26):
        next = trie[cur].children[i]
        if next == -1:
            continue
        if cur == root:
            trie[next].pi = root
        else:
            x = trie[cur].pi
            while x != root and trie[x].children[i] == -1:
                x = trie[x].pi
            if trie[x].children[i] != -1:
                x = trie[x].children[i]
            trie[next].pi = x
        pi = trie[next].pi
        trie[next].valid |= trie[pi].valid
        Q.append(next)


def aho_corashic(s, node, root, trie):
    ok = False
    for i in range(len(s)):
        c = ord(s[i]) - ord('a')
        while node != root and trie[node].children[c] == -1:
            node = trie[node].pi
        if trie[node].children[c] != -1:
            node = trie[node].children[c]
        if trie[node].valid:
            print('YES')
            return
    print('NO')
    return


m = int(sys.stdin.readline())
for i in range(m):
    s = sys.stdin.readline().rstrip()
    aho_corashic(s, node, root, trie)
