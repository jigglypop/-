import sys
from collections import deque
sys.stdin = open('./text/2311.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
def edge(a, b, c):
    C[a][b] = 1
    W[a][b] = c
    W[b][a] = -c
    graph[a].append(b)
    graph[b].append(a)


N, M = Split()
C = [[0] * (2 * N) for _ in range(2 * N)]
W = [[0] * (2 * N) for _ in range(2 * N)]
F = [[0] * (2 * N) for _ in range(2 * N)]
graph = [[] for _ in range(2* N)]

for i in range(M):
    a, b, c = Split()
    edge(2 * (a - 1) + 1, 2 * (b - 1), c)
    edge(2 * (b - 1) + 1, 2 * (a - 1), c)

for i in range( N):
    a, b = i * 2, i * 2 + 1
    C[a][b] = INF
    graph[a].append(b)
    graph[b].append(a)

S = 1
E = 2 *  (N - 1)
cost = 0
for i in range(2):
    prev = [-1] * (2 *  N)
    dp = [INF] * (2 *  N)
    inQ = [0] * (2 *  N)
    Q = deque([S])
    dp[S] = 0
    inQ[S] = 1
    while Q:
        x = Q.popleft()
        inQ[x]=0
        for v in graph[x]:
            if C[x][v] - F[x][v]>0 and dp[v] > dp[x] + W[x][v]:
                dp[v] = dp[x] + W[x][v]
                prev[v] = x
                if inQ[v] == 0:
                    Q.append(v)
                    inQ[v] = 1
    if prev[E]==-1:
        break
    u = E
    while u!=S:
        v = prev[u]
        F[v][u] += 1
        F[u][v] -= 1
        cost += W[v][u]
        u = v
print(cost)