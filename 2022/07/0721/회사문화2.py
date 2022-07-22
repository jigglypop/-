import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('./text/14268.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def dfs(u):
    global timer
    timer += 1
    tin[u] = timer
    for v in graph[u]:
        dfs(v)
    tout[u] = timer

def propagate(x, s, e):
    if lazy[x] != 0:
        tree[x] += lazy[x] * (e - s + 1)
        if s != e:
            lazy[x * 2] += lazy[x]
            lazy[x * 2 + 1] += lazy[x]
        lazy[x] = 0

def update(x, s, e, S, E, diff):
    propagate(x, s, e)
    if s > E or S > e:
        return
    if S <= s and e <= E:
        lazy[x] = diff
        propagate(x, s, e)
        return
    m = (s+e)//2
    update(x * 2, s, m, S, E, diff)
    update(x * 2 + 1, m + 1, e, S, E, diff)
    tree[x] = tree[x * 2] + tree[x * 2 + 1]

def query(x, s, e, S, E):
    propagate(x, s, e)
    if s > E or S > e:
        return 0
    if S <= s and e <= E:
        return tree[x]
    m = (s + e) // 2
    return query(x * 2, s, m, S, E) + query(x * 2 + 1, m + 1, e, S, E)

N, M = Split()
graph = [[] for _ in range(N)]
D = List()
for i in range(1, N):
    graph[D[i]-1].append(i)

tree = [0] * (4 * N)
lazy = [0] * (4 * N)
tin = [0] * (N + 1)
tout = [0] * (N + 1)
timer = -1
dfs(0)

for _ in range(M):
    temp = List()
    if temp[0] == 1:
        a, b = temp[1], temp[2]
        a -= 1
        update(1, 0, N - 1, tin[a], tout[a], b)
    else:
        a = temp[1] - 1
        print(query(1, 0, N - 1, tin[a], tin[a]))