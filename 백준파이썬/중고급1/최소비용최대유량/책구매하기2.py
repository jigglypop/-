import sys
from collections import deque
from pprint import pprint
sys.stdin = open('11406.txt', 'r')
input = sys.stdin.readline
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
books = [list(map(int, input().split())) for _ in range(Y)]
S = X + Y
E = X + Y + 1
C = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
F = [[0] * (X + Y + 2) for _ in range(X + Y + 2)]
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
        graph[x + Y].append(y)
        graph[y].append(x + Y)


total = 0
while True:
    Q = deque([S])
    parent = [-1 for _ in range(X + Y + 2)]
    while Q and parent[E] == -1:
        u = Q.popleft()
        for v in graph[u]:
            if parent[v] == -1 and C[u][v] > F[u][v]:
                parent[v] = u
                Q.append(v)
    if parent[E] == -1:
        break
    flow = sys.maxsize
    x = E
    while x != S:
        flow = min(flow, C[parent[x]][x] - F[parent[x]][x])
        x = parent[x]
    x = E
    while x != S:
        F[parent[x]][x] += flow
        F[x][parent[x]] -= flow
        x = parent[x]
    total += flow
print(total)
