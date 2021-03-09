import sys
from collections import deque
sys.stdin = open('11405.txt', "r")
INF = sys.maxsize
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
books = [list(map(int, input().split())) for _ in range(Y)]
S = X + Y
E = X + Y + 1
C = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
F = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
cost = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
graph = [[] for _ in range(X + Y + 2)]
for i in range(X):
    C[i + Y][E] = A[i]
    graph[i + Y].append(E)
    graph[E].append(i + Y)

for i in range(Y):
    C[S][i] = B[i]
    graph[i].append(S)
    graph[S].append(i)

for y in range(Y):
    for x in range(X):
        C[y][x + Y] = INF
        cost[y][x + Y] = books[y][x]
        cost[x + Y][y] = -cost[y][x + Y]
        graph[x + Y].append(y)
        graph[y].append(x + Y)

result = 0
while True:
    Q = deque([S])
    parent = [-1] * (X + Y + 2)
    dist = [INF] * (X + Y + 2)
    dist[S] = 0
    inQ = [False] * (X + Y + 2)
    inQ[S] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
    if parent[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[parent[x]][x] - F[parent[x]][x])
        x = parent[x]
    x = E
    while x != S:
        result += flow * cost[parent[x]][x]
        F[parent[x]][x] += flow
        F[x][parent[x]] -= flow
        x = parent[x]
print(result)
