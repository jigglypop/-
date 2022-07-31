import sys
from math import ceil, log2
sys.stdin = open('./text/1395.txt', 'r')
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline
N, M = Split()
tree = [0] * (4 * N)
lazy = [0] * (4 * N)

def propagate(x, s, e):
    if lazy[x] != 0:
        if lazy[x] % 2 == 1:
            tree[x] = (e - s + 1) - tree[x]
        if s != e:
            lazy[2 * x] += lazy[x]
            lazy[2 * x + 1] += lazy[x]
        lazy[x] = 0


def update(x, s, e, S, E, diff):
    propagate(x, s, e)
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
    propagate(x, s, e)
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return query(2 * x, s, mid, S, E) + query(2 * x + 1, mid + 1, e, S, E)


for _ in range(M):
    a, b, c = Split()
    if a == 0:
        update(1, 0, N-1, b-1, c-1, 1)
    else:
        print(query(1, 0, N-1, b-1, c-1))