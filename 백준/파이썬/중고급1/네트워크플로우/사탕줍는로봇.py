import sys
from collections import deque
from pprint import pprint
sys.stdin = open('15892.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
C = [[0] * (n+1) for _ in range(n+1)]
F = [[0] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    C[a][b] += c
    C[b][a] += c
    graph[a].append(b)
    graph[b].append(a)

total = 0
s = 1
t = n
while True:
    Q = deque([s])
    prev = [-1 for _ in range(n+1)]
    while Q and prev[t] == -1:
        u = Q.popleft()
        for v in graph[u]:
            if prev[v] == -1 and C[u][v] > F[u][v]:
                Q.append(v)
                prev[v] = u
    if prev[t] == -1:
        break
    flow = sys.maxsize
    x = t
    while x != s:
        flow = min(flow, C[prev[x]][x] - F[prev[x]][x])
        x = prev[x]
    x = t
    while x != s:
        F[prev[x]][x] += flow
        F[x][prev[x]] -= flow
        x = prev[x]
    total += flow
print(total)
