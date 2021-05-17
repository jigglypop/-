import sys
sys.stdin = open("11505.txt", "r")
input = sys.stdin.readline

P = 1000000007
N, M, K = map(int, input().split())
tree = [0] * N + [int(input()) for _ in range(N)]

for i in reversed(range(1, N)):
    tree[i] = (tree[2 * i] * tree[2 * i ^ 1]) % P


def update(i, x):
    tree[i] = x
    while i > 1:
        tree[i // 2] = (tree[i] * tree[i ^ 1]) % P
        i //= 2


def query(l, r):
    res = 1
    while l < r:
        if l % 2:
            res = (res * tree[l]) % P
            l += 1
        if not (r % 2):
            res = (res * tree[r]) % P
            r -= 1
        l >>= 1
        r >>= 1
    if l == r:
        res = (res * tree[l]) % P
    return res


for _ in range(M + K):
    a, b, c = map(int, input().split())
    b += N - 1
    if a == 1:
        update(b, c)
    else:
        c += N - 1
        print(query(b, c))
