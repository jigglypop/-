import sys
from pprint import pprint
sys.stdin = open("14725.txt", "r")
input = sys.stdin.readline


class Trie:
    head = {}

    def add(self, words):
        _head = self.head
        for word in words:
            if word not in _head:
                _head[word] = {}
            _head = _head[word]
        _head['*'] = True

    def search(self, words):
        _head = self.head
        for word in words:
            if word not in _head:
                return False
            _head = _head[word]
        return True if _head['*'] else False


N = int(input())
word_set = [list(input().split())[1:] for _ in range(N)]
trie = Trie()
for words in word_set:
    trie.add(words)


def solve(heads, k):
    if '*' in heads:
        return
    keys = list(heads.keys())
    keys.sort()
    for key in keys:
        value = heads[key]
        print('--' * k + str(key))
        solve(value, k+1)


heads = trie.head
solve(heads, 0)
