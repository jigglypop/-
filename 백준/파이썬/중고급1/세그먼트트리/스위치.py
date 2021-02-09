import sys
from math import ceil, log2
sys.stdin = open('1395.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
H = int(ceil(log2(N)))
tree = [0] * (1 << (H+1))
lazy = [0] * (1 << (H+1))


def lazy_update(x, s, e):
    if lazy[x] != 0:
        if lazy[x] % 2 == 1:
            tree[x] = (e - s + 1) - tree[x]
        if s != e:
            lazy[2 * x] += lazy[x]
            lazy[2 * x + 1] += lazy[x]
        lazy[x] = 0


def update(x, s, e, S, E, diff):
    lazy_update(x, s, e)
    if S > e or s > E:
        return
    if S <= s and e <= E:
        if diff % 2 == 1:
            tree[x] = (e - s + 1) - tree[x]
        if s != e:
            lazy[2 * x] += diff
            lazy[2 * x + 1] += diff
        return
    mid = (s + e) // 2
    update(2 * x, s, mid, S, E, diff)
    update(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] + tree[2 * x + 1]


def query(x, s, e, S, E):
    lazy_update(x, s, e)
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return query(2 * x, s, mid, S, E) + query(2 * x + 1, mid + 1, e, S, E)


for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        update(1, 0, N-1, b-1, c-1, 1)
    else:
        print(query(1, 0, N-1, b-1, c-1))
