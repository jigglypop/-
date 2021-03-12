from collections import deque
import sys
sys.stdin = open('2316.txt', 'r')
input = sys.stdin.readline
n, p = map(int, input().split())
C = [[0] * (2 * n) for _ in range(2 * n)]
F = [[0] * (2 * n) for _ in range(2 * n)]
graph = [[] for _ in range(2*n)]

for i in range(p):
    a, b = map(int, input().split())
    a = (a - 1) * 2 + 1
    b = (b - 1) * 2
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)
    C[b+1][a-1] = 1
    graph[b+1].append(a-1)
    graph[a-1].append(b+1)

for i in range(n):
    a, b = i * 2, i * 2 + 1
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)

S, E = 1, 2
result = 0
while True:
    Q = deque([S])
    parent = [-1] * (2 * n)
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if parent[v] == -1 and C[u][v] > F[u][v]:
                parent[v] = u
                Q.append(v)
    if parent[E] == -1:
        break
    x = E
    while x != S:
        F[parent[x]][x] += 1
        F[x][parent[x]] -= 1
        x = parent[x]
    result += 1
print(result)
