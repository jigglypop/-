import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/3604.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
while True:
    try:
        n, M = map(int, input().split())
    except:
        break
    N = 2 * n
    C = [[0] * (N + 2) for _ in range(N + 2)]
    F = [[0] * (N + 2) for _ in range(N + 2)]
    cost = [[0] * (N + 2) for _ in range(N + 2)]
    graph = [[] for _ in range(N + 2)]
    S, E = 0, N + 1
    total = [0]
    print(S, E)

    def edge(a, b, f, w):
        C[a][b] = f
        cost[a][b] = w
        cost[b][a] = -w
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(M):
        a, b, c = map(int, input().split())
        A = 2 * a - 1
        _A = 2 * a
        B = 2 * b - 1 
        _B = 2 * b
        edge(_A, B, 1, c)
    for i in range(2, n):
        edge(2 * i - 1, 2 * i, 1, 0)
    edge(1, 2, 2, 0)
    edge(0, 1, 2, 0)
    edge(N, N + 1, 2, 0)
    edge(N - 1, N, 2, 0)
    def spfa():
        Q = deque([S])
        dist = [INF] * (N + 2)
        inQ = [False] * (N + 2)
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
                        inQ[v] = True
                        Q.append(v)

    def find(v, f):
        if v == S:return f
        u = parent[v]
        return find(u, min(f, C[u][v] - F[u][v]))

    def flow(v, f):
        if v == S: return
        u = parent[v]
        total[0] += f * cost[u][v] 
        F[u][v] += f
        F[v][u] -= f
        flow(u, f)

    while True:
        parent = [0] * (N + 2)
        spfa()
        if not parent[E]: break
        f = find(E, INF)
        flow(E, f)
    print(total[0])