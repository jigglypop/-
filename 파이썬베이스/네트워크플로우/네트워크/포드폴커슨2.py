import sys
from collections import deque
sys.stdin = open('17412.txt', 'r')
input = sys.stdin.readline
N, P = map(int, input().split())
c = [[0] * (N+1) for _ in range(N+1)]
f = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
S, E = 1, 2
total = 0
for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    c[a][b] = 1

def bfs():
    Q = deque([S])
    while Q and not visited[E]:
        u = Q.popleft()
        for v in graph[u]:
            if not visited[v] and c[u][v] > f[u][v]:
                visited[v] = u
                Q.append(v)

def flow(v):
    if v == S:return
    u = visited[v]
    f[u][v] += 1
    f[v][u] -= 1
    flow(u)

while True:
    visited = [0] * (N + 1)
    bfs()
    if not visited[E]:break
    flow(E)
    total += 1
print(total)
