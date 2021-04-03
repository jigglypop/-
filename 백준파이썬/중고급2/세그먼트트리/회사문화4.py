import sys
from math import ceil, log2
sys.stdin = open('14288.txt', 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
children = [[] for _ in range(n)]
D = list(map(int, input().split()))
for i in range(1, n):
    children[D[i] - 1].append(i)


H = int(ceil(log2(n)))
tree = [0] * (1 << (H+1))
lazy = [0] * (1 << (H+1))
tin = [0] * n
tout = [0] * n
timer = -1


def dfs(u):
    global timer
    timer += 1
    tin[u] = timer
    for v in children[u]:
        dfs(v)
    tout[u] = timer


dfs(0)


def lazy_update(x, s, e):
    if lazy[x] != 0:
        tree[x] += lazy[x] * (e - s + 1)
        if s != e:
            lazy[2*x] += lazy[x]
            lazy[2*x + 1] += lazy[x]
        lazy[x] = 0


def update_range(x, s, e, S, E, diff):
    lazy_update(x, s, e)
    if s > E or S > e:
        return
    if S <= s and e <= E:
        lazy[x] += diff
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
    return query(x * 2, s, mid,  S, E) + query(x * 2 + 1, mid + 1, e, S, E)


di = True
for _ in range(m):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        a, b = temp[1], temp[2]
        a -= 1
        if di:
            update_range(1, 0, n-1, tin[a], tout[a], b)
        else:
            update_range(1, 0, n-1, tin[a], tin[a], b)
    elif temp[0] == 2:
        a = temp[1] - 1
        if di:
            print(query(1, 0, n-1, tin[a], tin[a]))
        else:
            print(query(1, 0, n-1, tin[a], tout[a]))
    else:
        di = not di
print(tree)
