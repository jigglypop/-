import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('./text/14287.txt', 'r')
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

def propagate(n, s, e):
    if lazy[n] != 0:
        tree[n] += lazy[n] * (e - s + 1)
        if s != e:
            lazy[2 * n] += lazy[n]
            lazy[2 * n + 1] += lazy[n]
        lazy[n] = 0

def update(n, s, e, S, E, diff):
    propagate(n, s, e)
    if s > E or S > e:
        return
    if S <= s and e <= E:
        lazy[n] = diff
        propagate(n, s, e)
        return
    m = (s + e)//2
    update(2 * n, s, m, S, E, diff)
    update(2 * n + 1, m + 1, e, S, E, diff)
    tree[n] = tree[2 * n] + tree[2 * n + 1]

def query(n, s, e, S, E):
    propagate(n, s, e)
    if s > E or S > e:
        return 0
    if S <= s and e <= E:
        return tree[n]
    m = (s + e) // 2
    return query(2 * n, s, m, S, E) + query(2 * n + 1, m + 1, e, S, E)

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
        update(1, 0, N - 1, tin[a], tin[a], b)
    else:
        a = temp[1] - 1
        print(query(1, 0, N - 1, tin[a], tout[a]))