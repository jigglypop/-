import sys
from collections import deque
sys.stdin = open('17412.txt', 'r')
input = sys.stdin.readline
N, P = map(int, input().split())
c = [[0] * (N+1) for _ in range(N+1)]
f = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(P):
    a, b = map(int, input().split())
    graph[a].append(b)
    c[a][b] = 1

start, end = 1, 2
total = 0
while True:
    visited = [0]*(N+1)
    Q = deque([(start)])
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if not visited[v] and c[u][v] > f[u][v]:
                visited[v] = u
                Q.append(v)
            if v == end:
                break
    if not visited[end]:
        break
    v = end
    while v != start:
        u = visited[v]
        f[u][v] += 1
        v = u
    total += 1

print(total)
