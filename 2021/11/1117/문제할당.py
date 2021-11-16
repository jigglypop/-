import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/1258.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
N = 2 * n + 2
table = [list(map(int, input().split())) for _ in range(n)]
C = [[0] * N for _ in range(N)]
F = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
S, E = 0, N - 1
graph = [[i + 1 for i in range(n)]] + [[0] + [i + n + 1 for i in range(n)] for _ in range(n)] + [[E] + [i + 1 for i in range(n)] for _ in range(n)]+ [[i + n + 1 for i in range(n)]]
total = [0]
for y in range(n):
    for x in range(n):
        p = y + 1
        q = x + n + 1
        C[p][q] = 1
        cost[p][q] = table[y][x]
        cost[q][p] = -table[y][x]
for i in range(n):
    C[S][i + 1] = 1
    C[i + n + 1][E] = 1

def spfa():
    Q = deque([S])
    dist = [INF] * N
    inQ = [False] * N
    dist[S] = 0
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
    parent = [0] * N
    spfa()
    if not parent[E]: break
    f = find(E, INF)
    flow(E, f)
print(total[0])