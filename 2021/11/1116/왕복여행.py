import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/2311.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
C = [[0] * (N + 1) for _ in range(N + 1)]
F = [[0] * (N + 1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
S, E = 1, N
total = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    C[a][b] = c

def bfs():
    Q = deque([S])
    while Q and not visited[E]:
        u = Q.popleft()
        for v in graph[u]:
            if not visited[v] and C[u][v] > F[u][v]:
                visited[v] = u
                Q.append(v)

def flow(v, f):
    if v == S:return
    u = visited[v]
    F[u][v] += f
    F[v][u] -= f
    flow(u, f)

def find(v, f):
    if v == S:
        return f
    u = visited[v]
    return find(u, min(f, C[u][v] - F[u][v]))

while True:
    visited = [0] * (N + 1)
    bfs()
    if not visited[E]: break
    f = find(E, INF)
    print(visited)
    flow(E, f)
    total += f
print(total)
    