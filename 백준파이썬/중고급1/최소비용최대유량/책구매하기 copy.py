import sys
from collections import deque
sys.stdin = open('11405.txt')
INF = sys.maxsize
n, m = map(int, input().split())
max_n = 100
max_v = 2 * (max_n+1)
S = max_v-2
E = max_v-1
C = [[0] * max_v for _ in range(max_v)]
d = [[0] * max_v for _ in range(max_v)]
F = [[0] * max_v for _ in range(max_v)]
graph = [[] for _ in range(max_v)]
A = list(map(int, input().split()))
for i in range(max_n, max_n+n):
    C[i][E] = A[i-max_n]
    graph[i].append(E)
    graph[E].append(i)
B = list(map(int, input().split()))
for i in range(m):
    C[S][i] = B[i]
    graph[S].append(i)
    graph[i].append(S)
D = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(max_n, max_n+n):
        d[i][j] = D[i][j-max_n]
        d[j][i] = -d[i][j]
        C[i][j] = INF
        graph[i].append(j)
        graph[j].append(i)
result = 0
while True:
    Q = deque([S])
    parent = [-1] * max_v
    dist = [INF] * max_v
    dist[S] = 0
    inQ = [0]*max_v
    inQ[S] = 1
    while Q:
        x = Q.popleft()
        inQ[x] = 0
        for v in graph[x]:
            if C[x][v]-F[x][v] > 0 and dist[v] > dist[x]+d[x][v]:
                dist[v] = dist[x]+d[x][v]
                parent[v] = x
                if inQ[v] == 0:
                    Q.append(v)
                    inQ[v] = 1
    if parent[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[parent[x]][x]-F[parent[x]][x])
        x = parent[x]
    x = E
    while x != S:
        result += flow * d[parent[x]][x]
        F[parent[x]][x] += flow
        F[x][parent[x]] -= flow
        x = parent[x]
print(result)
