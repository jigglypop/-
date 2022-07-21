import sys
sys.stdin = open('./text/14275.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

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