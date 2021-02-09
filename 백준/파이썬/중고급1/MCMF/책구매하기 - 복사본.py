import sys
from collections import deque
sys.stdin = open('11405.txt')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m = map(int, input().split())
s = n + m
e = n + m + 1
total = n + m + 2
INF = sys.maxsize

graph = [[]for _ in range(total)]
C = [[0] * total for _ in range(total)]
flow = [[0] * total for _ in range(total)]
d = [[0] * total for _ in range(total)]

left = list(range(m))
right = list(range(m, n+m))
graph[s] = left
graph[e] = right

for u in range(m):
    graph[u] = right+[s]
for u in range(m, n+m):
    graph[u] = left+[e]

for i, cap in enumerate(map(int, input().split())):
    i += m
    C[i][e] = cap
for i, cap in enumerate(map(int, input().split())):
    C[s][i] = cap

for i in range(m):
    for j, dist in enumerate(map(int, input().split())):
        j += m
        d[i][j] = dist
        d[j][i] = -dist
        C[i][j] = INF


def SPFA(s, e):
    dist = [INF]*total
    dist[s] = 0
    prev = [-1]*total
    inq = [False]*total
    Q = deque([s])
    while Q:
        u = Q.popleft()
        inq[u] = False
        for v in graph[u]:
            if C[u][v] - flow[u][v] > 0 and dist[v] > dist[u] + d[u][v]:
                dist[v] = dist[u]+d[u][v]
                prev[v] = u
                if not inq[v]:
                    Q.append(v)
                    inq[v] = True
    return prev


def MCMF(s, e, prev):
    v = e
    flow = INF
    res = 0
    while v != s:
        u = prev[v]
        flow = min(flow, C[u][v]-flow[u][v])
        v = u
    v = e
    while v != s:
        u = prev[v]
        res += (d[u][v]*flow)
        flow[u][v] += flow
        flow[v][u] -= flow
        v = u
    return res


result = 0
while True:
    prev = SPFA(s, e)
    if prev[e] == -1:
        break
    result += MCMF(s, e, prev)
print(result)
