import sys
from collections import deque
sys.stdin = open('./text/11405.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
X, Y = Split()
A = List()
B = List()
books = [List() for _ in range(Y)]
S = X + Y
E = X + Y + 1
C = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
F = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
W = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
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
        W[y][x + Y] = books[y][x]
        W[x + Y][y] = -W[y][x + Y]
        C[y][x + Y] = INF
        graph[x + Y].append(y)
        graph[y].append(x + Y)

def SPFA():
    Q = deque([S])
    prev = [-1] * (X + Y + 2)
    dp = [INF] * (X + Y + 2)
    dp[S] = 0
    inQ = [False] * (X + Y + 2)
    inQ[S] = True
    while Q:
        x = Q.popleft()
        inQ[x] = False
        for v in graph[x]:
            if C[x][v] - F[x][v] > 0 and dp[v] > dp[x] + W[x][v]:
                dp[v] = dp[x] + W[x][v]
                prev[v] = x
                if not inQ[v]:
                    Q.append(v)
                    inQ[v] = True
    return prev

result = 0
while True:
    prev = SPFA()
    if prev[E] == -1:
        break
    flow = INF
    x = E
    while x != S:
        flow = min(flow, C[prev[x]][x] - F[prev[x]][x])
        x = prev[x]
    x = E
    while x != S:
        result += flow * W[prev[x]][x]
        F[prev[x]][x] += flow
        F[x][prev[x]] -= flow
        x = prev[x]
print(result)