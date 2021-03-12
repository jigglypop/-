import sys
from math import ceil, log2
sys.stdin = open('14268.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(u):
    global timer
    timer += 1
    tin[u] = timer
    for v in children[u]:
        dfs(v)
    tout[u] = timer


def lazy_update(x, s, e):
    if lazy[x] != 0:
        tree[x] += lazy[x] * (e - s + 1)
        if s != e:
            lazy[x*2] += lazy[x]
            lazy[x*2+1] += lazy[x]
        lazy[x] = 0


def update_range(x, s, e, S, E, diff):
    lazy_update(x, s, e)
    if s > E or S > e:
        return
    if S <= s and e <= E:
        lazy[x] = diff
        lazy_update(x, s, e)
        return
    mid = (s+e)//2
    update_range(x * 2, s, mid, S, E, diff)
    update_range(x * 2 + 1, mid+1, e, S, E, diff)
    tree[x] = tree[x * 2] + tree[x * 2 + 1]


def query(x, s, e, S, E):
    lazy_update(x, s, e)
    if s > E or S > e:
        return 0
    if S <= s and e <= E:
        return tree[x]
    mid = (s + e) // 2
    return query(x * 2, s, mid, S, E) + query(x * 2 + 1, mid + 1, e, S, E)


n, m = map(int, input().split())
children = [[] for _ in range(n)]
D = list(map(int, input().split()))
for i in range(1, n):
    children[D[i]-1].append(i)
h = int(ceil(log2(n)))
tree = [0] * (1 << (h+1))
lazy = [0] * (1 << (h+1))
tin = [0] * (n + 1)
tout = [0] * (n + 1)
timer = -1
dfs(0)
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        a, b = temp[1], temp[2]
        a -= 1
        update_range(1, 0, n-1, tin[a], tout[a], b)
    else:
        a = temp[1]-1
        print(query(1, 0, n-1, tin[a], tin[a]))
