import sys
import collections


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


my = Trie()


def aho_corasick_failure():
    root = my.root
    trie = my.trie
    q = collections.deque()
    trie[root].pi = root
    q.append(root)
    while q:
        cur = q.popleft()
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
            q.append(next)


def aho_corasick(s):
    node = my.root
    trie = my.trie
    root = my.root
    ok = False
    for i in range(len(s)):
        c = ord(s[i]) - ord('a')
        while node != root and trie[node].children[c] == -1:
            node = trie[node].pi
        if trie[node].children[c] != -1:
            node = trie[node].children[c]
        if trie[node].valid:
            ok = True
    return ok


ans = []
n = int(sys.stdin.readline())
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    my.add(my.root, temp, 0)
aho_corasick_failure()
m = int(sys.stdin.readline())
for i in range(m):
    is_in = sys.stdin.readline().rstrip()
    if aho_corasick(is_in):
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)
