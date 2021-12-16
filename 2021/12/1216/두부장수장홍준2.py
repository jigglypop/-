import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/11111.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
score = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]
]
di = ((0, 1), (0, -1), (1, 0), (-1, 0))
Y, X = map(int,input().split())
N = Y * X + 2
S, E = N - 2, N - 1
total = [0]
C = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
F = [[0]  *N for _ in range(N)]
graph=[[] for _ in range(N)]
board = [[*input()] for _ in range(Y)]
for i in range(Y):
    for j in range(X):
        board[i][j] = ord(board[i][j]) - 65 if board[i][j] != 'F' else 4

def edge(a, b):
    C[a][b]=1
    graph[a].append(b)
    graph[b].append(a)

for y in range(Y):
    for x in range(X):
        a = y * X + x
        if (y + x) % 2 == 0:
            edge(S, a)
            edge(a, E)
            for dy, dx in di:
                nx, ny= y + dy, x + dx
                b = nx * X + ny
                if 0 <= nx < Y and 0 <= ny < X:
                    edge(a, b)
                    cost[a][b] = -score[board[y][x]][board[nx][ny]]
                    cost[b][a] = -cost[a][b]
        else:
            edge(a, E)

def spfa():
    Q = deque([S])
    dist = [INF] * N
    inQ = [False] * N
    dist[S] = 0
    inQ[S] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dist[v] > dist[u] + cost[u][v]:
                dist[v] = dist[u] + cost[u][v]
                parent[v] = u
                if not inQ[v]:
                    inQ[v] = True
                    Q.append(v)

def find(v, f):
    if v == S:
        return f
    u = parent[v]
    return find(u, min(f, C[u][v] - F[u][v]))

def flow(v, f):
    if v == S:
        return
    u = parent[v]
    total[0] += f * cost[u][v]
    F[u][v] += f
    F[v][u] -= f
    flow(u, f)

while True:
    parent = [0] * N
    spfa()
    if not parent[E]: break
    f = find(E, INF)
    flow(E, f)
print(-total[0])