import sys
sys.stdin = open("./text/1306.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
tree = [0] * N + list(map(int, input().strip().split()))
for i in reversed(range(1, N)):
    tree[i] = max(tree[i * 2], tree[i * 2 ^ 1])

def query(l, r):
    l += N - 1
    r += N - 1
    result = 0
    while l <= r:
        if l % 2:
            result = max(result, tree[l])
            l += 1
        if not r % 2:
            result = max(result, tree[r])
            r -= 1
        l >>= 1
        r >>= 1
    return result

for i in range(M, N - M + 2):
    print(query(i - M + 1, i + M - 1), end=" ")