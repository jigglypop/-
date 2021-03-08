from collections import deque
import sys
sys.stdin = open('2316.txt', 'r')


input = sys.stdin.readline
n, p = map(int, input().split())
C = [[0] * (2 * n) for _ in range(2 * n)]
F = [[0] * (2 * n) for _ in range(2 * n)]
graph = [[] for _ in range(2 * n)]

for i in range(p):
    a, b = map(int, input().split())
    a = (a - 1) * 2 + 1
    b = (b - 1) * 2
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
    C[b+1][a-1] = 1
    graph[b+1].append(a-1)
    graph[a-1].append(b+1)

for i in range(n):
    a, b = i * 2, i * 2 + 1
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(u, limit):
    if limit <= 0:
        return 0
    if u == E:
        return limit
    val = 0
    for v in graph[u]:
        res = C[u][v] - F[u][v]
        if level[v] == level[u] + 1 and res > 0:
            flow = dfs(v, min(limit - val, res))
            F[u][v] += flow
            F[v][u] -= flow
            val += flow
    if val == 0:
        level[u] -= 1
    return val


S, E = 1, 2
total = 0
while True:
    Q = deque([S])
    level = [-1] * len(graph)
    level[S] = 0
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if level[v] == -1 and C[u][v] > F[u][v]:
                level[v] = level[u] + 1
                Q.append(v)
    if level[E] == -1:
        break
    total += dfs(S, sum(C[S][v] for v in graph[S]))
print(total)
