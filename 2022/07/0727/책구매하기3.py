
import sys
from collections import deque
sys.stdin = open('./text/11407.txt', 'r')
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
costs = [List() for _ in range(Y)]
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
        C[y][x + Y] = books[y][x]
        cost[y][x + Y] = costs[y][x]
        cost[x + Y][y] = -costs[y][x]
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
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dp[v] > dp[u] + cost[u][v]:
                dp[v] = dp[u] + cost[u][v]
                prev[v] = u
                if not inQ[v]:
                    inQ[v] = True
                    Q.append(v)
    return prev

def FIND(u):
    global flow
    if u == S: return
    v = prev[u]
    flow = min(flow, C[v][u] - F[v][u])
    FIND(v)

def FLOW(u):
    global flow, total
    if u == S: return
    v = prev[u]
    F[v][u] += flow
    F[u][v] -= flow
    FLOW(v)
    total += flow * cost[v][u]

count = 0
total = 0
while True:
    prev = SPFA()
    if prev[E] == -1: break
    flow = INF
    FIND(E)
    FLOW(E)
    count += flow
    
print(count)
print(total)