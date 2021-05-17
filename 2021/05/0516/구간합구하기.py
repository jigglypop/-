import sys
sys.stdin = open("2042.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
tree = [0] * n + [int(input()) for _ in range(n)]
for i in reversed(range(1, n)):
    tree[i] = tree[2 * i] + tree[2 * i ^ 1]


def update(i, x):
    tree[i] = x
    while i > 1:
        tree[i // 2] = tree[i] + tree[i ^ 1]
        i //= 2


def query(l, r):
    res = 0
    while l < r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1:
            r -= 1
            res += tree[r]
        l //= 2
        r //= 2
    return res


for _ in range(m + k):
    a, b, c = map(int, input().split())
    b += n - 1
    if a == 1:
        update(b, c)
    else:
        c += n
        print(query(b, c))
