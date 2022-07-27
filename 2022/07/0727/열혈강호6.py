import sys
from collections import deque
sys.stdin = open('./text/11409.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
X, Y = Split()
S = X + Y
E = X + Y + 1
C = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
F = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
cost = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
graph = [[] for _ in range(X + Y + 2)]
for i in range(X):
    C[S][i] = 1
    graph[S].append(i)
    graph[i].append(S)
for i in range(Y):
    C[i + X][E] = 1
    graph[i + X].append(E)
    graph[E].append(i + X)

for i in range(X):
    temp = List()
    jobs = [temp[i:i + 2] for i in range(1, len(temp), 2)]
    for job in jobs:
        j, c = job
        j -= 1
        C[i][j + X] = 1
        cost[i][j + X] = -c
        cost[j + X][i] = c
        graph[i].append(j + X)
        graph[j + X].append(i)


def SPFA():
    Q = deque([S])
    prev = [-1] * (X + Y + 2)
    dp = [INF] * (X + Y + 2)
    dp[S] = 0
    inQ = [False] * (X + Y + 2)
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
    return prev

count = 0
total = 0
while True:
    prev = SPFA()
    if prev[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[prev[x]][x]-F[prev[x]][x])
        x = prev[x]
    x = E
    while x != S:
        total += flow * cost[prev[x]][x]
        F[prev[x]][x] += flow
        F[x][prev[x]] -= flow
        x = prev[x]
    count += 1
print(count)
print(-total)