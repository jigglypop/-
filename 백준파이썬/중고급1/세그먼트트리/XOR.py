import sys
from math import ceil, log2
sys.stdin = open('12844.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
H = int(ceil(log2(N)))
A = list(map(int, input().split()))
tree = [0] * (1 << (H+1))
lazy = [0] * (1 << (H+1))


def init(x, s, e):
    if s == e:
        tree[x] = A[s]
        return tree[x]
    mid = (s + e) // 2
    tree[x] = init(2 * x, s, mid) ^ init(2 * x + 1, mid + 1, e)
    return tree[x]


def update_lazy(x, s, e):
    if lazy[x] == 0:
        return
    L = (e - s + 1)
    if L % 2 == 1:
        tree[x] ^= lazy[x]
    if s != e:
        lazy[2 * x] ^= lazy[x]
        lazy[2 * x + 1] ^= lazy[x]
    lazy[x] = 0


def update_range(x, s, e, S, E, diff):
    update_lazy(x, s, e)
    if S > e or s > E:
        return
    if S <= s and e <= E:
        L = (e - s + 1)
        if L % 2 == 1:
            tree[x] ^= diff
        if s != e:
            lazy[2 * x] ^= diff
            lazy[2 * x + 1] ^= diff
        return
    mid = (s + e) // 2
    update_range(2 * x, s, mid, S, E, diff)
    update_range(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] ^ tree[2 * x + 1]


def query(x, s, e, S, E):
    update_lazy(x, s, e)
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return query(2 * x, s, mid, S, E) ^ query(2 * x + 1, mid + 1, e, S, E)


init(1, 0, N-1)
M = int(input())
for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        a, b, c, d = temp
        update_range(1, 0, N-1, min(b, c), max(b, c), d)
    else:
        a, b, c = temp
        print(query(1, 0, N-1, min(b, c), max(b, c)))
