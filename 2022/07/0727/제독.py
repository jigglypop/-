

import sys
from collections import deque
sys.stdin = open('./text/3640.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
while True:
    try:
        n, M = Split()
    except:
        break
    N = 2 * n
    C = [[0] * (N + 2) for _ in range(N + 2)]
    F = [[0] * (N + 2) for _ in range(N + 2)]
    cost = [[0] * (N + 2) for _ in range(N + 2)]
    graph = [[] for _ in range(N + 2)]
    S, E = 0, N + 1
    total = [0]
    def edge(a, b, f, w):
        C[a][b] = f
        cost[a][b] = w
        cost[b][a] = -w
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(M):
        a, b, c = Split()
        A = 2 * a - 1
        _A = 2 * a
        B = 2 * b - 1 
        edge(_A, B, 1, c)

    for i in range(2, n):
        edge(2 * i - 1, 2 * i, 1, 0)
    edge(1, 2, 2, 0)
    edge(0, 1, 2, 0)
    edge(N, N + 1, 2, 0)
    edge(N - 1, N, 2, 0)

    def SPFA():
        Q = deque([S])
        dp = [INF] * (N + 2)
        inQ = [False] * (N + 2)
        dp[S] = 0
        inQ[S] = True
        while Q:
            u = Q.popleft()
            inQ[u] = False
            for v in graph[u]:
                if C[u][v] > F[u][v] and dp[v] > dp[u] + cost[u][v]:
                    dp[v] = dp[u] + cost[u][v]
                    prev[v] = u
                    if not inQ[v]:
                        inQ[v] = True
                        Q.append(v)

    def find(v, f):
        if v == S:
            return f
        u = prev[v]
        return find(u, min(f, C[u][v] - F[u][v]))

    def flow(v, f):
        if v == S: 
            return
        u = prev[v]
        total[0] += f * cost[u][v] 
        F[u][v] += f
        F[v][u] -= f
        flow(u, f)

    while True:
        prev = [0] * (N + 2)
        SPFA()
        if not prev[E]: break
        f = find(E, INF)
        flow(E, f)
    print(total[0])