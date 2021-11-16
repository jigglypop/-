import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/2311.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
C = [[0] * (N + 2) for _ in range(N + 2)]
F = [[0] * (N + 2) for _ in range(N + 2)]
cost = [[0] * (N + 2) for _ in range(N + 2)]
graph = [[] for _ in range(N + 2)]
S, E = 0, N + 1
total = [0]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    C[a][b] = 1
    cost[a][b] = c
    cost[b][a] = c
graph[0].append(1)
graph[1].append(0)
graph[N].append(N + 1)
graph[N + 1].append(N)
C[0][1] = 2
C[N][N + 1] = 2

def spfa():
    Q = deque([S])
    dist = [INF] * (N + 2)
    inQ = [False] * (N + 2)
    inQ[S] = True
    dist[S] = 0
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not inQ[v]:
                    inQ[v] = True
                    Q.append(v)

def flow(v, f):
    if v == S:return
    u = parent[v]
    total[0] += f * cost[u][v]
    F[u][v] += f
    F[v][u] -= f
    flow(u, f)

def find(v, f):
    if v == S:return f
    u = parent[v]
    return find(u, min(f, C[u][v] - F[u][v]))

while True:
    parent = [0] * (N + 2)
    spfa()
    if not parent[E]: break
    f = find(E, INF)
    flow(E, f)
print(total[0])
    