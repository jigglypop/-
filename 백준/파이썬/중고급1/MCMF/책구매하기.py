import sys
from collections import deque
sys.stdin = open('11405.txt')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())
start = n + m
end = n + m + 1
total = n + m + 2
INF = sys.maxsize

graph = [[] for _ in range(total)]
C = [[0] * total for _ in range(total)]
flow = [[0] * total for _ in range(total)]
cost = [[0] * total for _ in range(total)]

left = list(range(m))
right = list(range(m, n+m))
graph[start] = left
graph[end] = right

for u in range(m):
    graph[u] = right + [start]
for u in range(m, n + m):
    graph[u] = left + [end]

for i, cap in enumerate(map(int, input().split())):
    i += m
    C[i][end] = cap
for i, cap in enumerate(map(int, input().split())):
    C[start][i] = cap

for i in range(m):
    for j, dist in enumerate(map(int, input().split())):
        j += m
        cost[i][j] = dist
        cost[j][i] = -dist
        C[i][j] = INF


def SPFA(start, end):
    dist = [INF] * total
    dist[start] = 0
    parent = [-1] * total
    inqueue = [False] * total
    Q = deque([start])
    while Q:
        u = Q.popleft()
        inqueue[u] = False
        for v in graph[u]:
            if C[u][v] - flow[u][v] > 0 and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not inqueue[v]:
                    Q.append(v)
                    inqueue[v] = True
    return parent


def MCMF(start, end, parent):
    v = end
    flow = INF
    result = 0
    while v != start:
        u = parent[v]
        flow = min(flow, C[u][v] - flow[u][v])
        v = u
    v = end
    while v != start:
        u = parent[v]
        result += (cost[u][v] * flow)
        flow[u][v] += flow
        flow[v][u] -= flow
        v = u
    return result


result = 0
while True:
    parent = SPFA(start, end)
    if parent[end] == -1:
        break
    result += MCMF(start, end, parent)
print(result)
