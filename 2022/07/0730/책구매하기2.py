import sys
from collections import deque
sys.stdin = open('./text/11406.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

X, Y = Split()
A = List()
B = List()
books = [List() for _ in range(Y)]
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

def bfs():
    Q = deque([S])
    prev = [-1 for _ in range(X + Y + 2)]
    while Q and prev[E] == -1:
        u = Q.popleft()
        for v in graph[u]:
            if prev[v] == -1 and C[u][v] > F[u][v]:
                prev[v] = u
                Q.append(v)
    return prev

total = 0
while True:
    prev = bfs()
    if prev[E] == -1:
        break
    flow = sys.maxsize
    x = E
    while x != S:
        flow = min(flow, C[prev[x]][x] - F[prev[x]][x])
        x = prev[x]
    x = E
    while x != S:
        F[prev[x]][x] += flow
        F[x][prev[x]] -= flow
        x = prev[x]
    total += flow
print(total)

