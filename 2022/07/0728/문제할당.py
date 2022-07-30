import sys
from collections import deque
sys.stdin = open('./text/1258.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
n = Int()
N = 2 * n + 2
table = [List() for _ in range(n)]
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

def SPFA():
    Q = deque([S])
    dp = [INF] * N
    inQ = [False] * N
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
                    Q.append(v)
                    inQ[v] = True

def flow(v, f):
    if v == S: return
    total[0] += f * cost[prev[v]][v]
    F[prev[v]][v] += f
    F[v][prev[v]] -= f
    flow(prev[v], f)

def find(v, f):
    if v == S: return f
    return find(prev[v], min(f, C[prev[v]][v] - F[prev[v]][v]))

while True:
    prev = [0] * N
    SPFA()
    if not prev[E]: break
    f = find(E, INF)
    flow(E, f)
print(total[0])