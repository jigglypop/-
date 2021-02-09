import sys
from math import ceil, log2
sys.stdin = open('14267.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
D = list(map(int, input().split()))
for i in range(1, n):
    g[D[i]-1].append(i)
tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = -1


def dfs(u):
    global timer
    timer += 1
    tin[u] = timer
    for v in g[u]:
        dfs(v)
    timer += 1
    tout[u] = timer


dfs(0)
H = int(ceil(log2(timer)))
tree = [0] * (1 << (H + 1))
lazy = [0] * (1 << (H + 1))


def update_lazy(x, s, e):
    if lazy[x] != 0:
        tree[x] = (e - s + 1) * lazy[x]
        if s != e:
            lazy[2 * x] += lazy[x]
            lazy[2 * x + 1] += lazy[x]
        lazy[x] = 0


def update_range(x, s, e, S, E, diff):
    update_lazy(x, s, e)
    if S > e or s > E:
        return
    if S <= s and e <= E:
        tree[x] += (e - s + 1) * diff
        if s != e:
            lazy[2 * x] += diff
            lazy[2 * x + 1] += diff
        return
    mid = (s + e) // 2
    update_range(2 * x, s, mid, S, E, diff)
    update_range(2 * x + 1, mid + 1, e, S, E, diff)
    tree[x] = tree[2 * x] + tree[2 * x + 1]


def query(x, s, e, i):
    update_lazy(x, s, e)
    if i > e or s > i:
        return 0
    if s == e and s == i:
        return tree[x]
    mid = (s + e)//2
    if i <= mid:
        return query(2 * x, s, mid, i)
    else:
        return query(2 * x + 1, mid + 1, e, i)


for _ in range(m):
    i, diff = map(int, input().split())
    update_range(1, 1, timer, tin[i], tout[i], diff)

for i in range(1, n+1):
    print(query(1, 1, timer, tout[i]), end=" ")
