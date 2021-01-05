import sys
sys.stdin = open('14425.txt', 'r')


class Trie:
    head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False


N, S = map(int, input().split())
trie = Trie()
for _ in range(N):
    trie.add(str(input()))
count = 0
for _ in range(S):
    count += trie.search(str(input()))
print(count)
