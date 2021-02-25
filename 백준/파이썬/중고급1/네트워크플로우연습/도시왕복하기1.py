from collections import deque
import sys
sys.stdin = open('17412.txt', 'r')
input = sys.stdin.readline
n, p = map(int, input().split())
graph = [[] for i in range(n+1)]
total = 0

C = [[0] * (n + 1) for _ in range(n+1)]
F = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(p):
    a, b = map(int, input().split())
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
s = 1
t = 2
while True:
    Q = deque([s])
    parent = [-1 for _ in range(n+1)]
    while Q and parent[t] == -1:
        u = Q.popleft()
        for v in graph[u]:
            if parent[v] == -1 and C[u][v] > F[u][v]:
                Q.append(v)
                parent[v] = u
    if parent[v] == -1:
        break
    x = t
    while x != s:
        F[parent[x]][x] += 1
        F[x][parent[x]] -= 1
        x = parent[x]
    total += 1
print(total)
