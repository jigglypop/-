import sys
sys.setrecursionlimit(10**4)
sys.stdin = open('./text/2150.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

V, E = Split()
board = [[] for _ in range(V + 1)]
rboard = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = Split()
    board[a].append(b)
    rboard[b].append(a)

def dfs(u, board, S):
    visited[u] = True
    for v in board[u]:
        if not visited[v]:
            dfs(v, board, S)
    S.append(u)

S = []
visited = [False] * (V + 1)
for i in range(1, V+1):
    if not visited[i]:
        dfs(i, board, S)

visited = [False] * (V+1)
results = []
while S:
    scc = []
    i = S.pop()
    if not visited[i]:
        dfs(i, rboard, scc)
        results.append(sorted(scc) + [-1])

results.sort()
print(len(results))
for r in results:
    print(*r)

