import sys
from collections import deque
sys.stdin = open('./text/14424.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

INF = sys.maxsize
score = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]
]
di = ((0, 1), (0, -1), (1, 0), (-1, 0))
Y, X = Split()
N = Y * X + 2
S, E = N - 2, N - 1
total = [0]
C = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
F = [[0] * N for _ in range(N)]
graph = [[] for _ in range(N)]
board = [[*Str()] for _ in range(Y)]
for i in range(Y):
    for j in range(X):
        board[i][j] = ord(board[i][j]) - 65 if board[i][j] != 'F' else 4

def edge(a, b):
    C[a][b] = 1
    graph[a].append(b)
    graph[b].append(a)

for y in range(Y):
    for x in range(X):
        a = y * X + x
        if (y + x) % 2 == 0:
            edge(S, a)
            edge(a, E)
            for dy, dx in di:
                nx, ny = y + dy, x + dx
                b = nx * X + ny
                if 0 <= nx < Y and 0 <= ny < X:
                    edge(a, b)
                    cost[a][b] = -score[board[y][x]][board[nx][ny]]
                    cost[b][a] = -cost[a][b]
        else:
            edge(a, E)

def SPFA():
    Q = deque([S])
    dp = [INF] * N
    inQ = [False] * N
    dp[S] = 0
    inQ[S] = True
    while Q:
        u = Q.popleft()
        inQ[u] = False
        for v in graph[u]:
            if C[u][v] > F[u][v] and dp[v] > dp[u] + cost[u][v]:
                dp[v] = dp[u] + cost[u][v]
                prev[v] = u
                if not inQ[v]:
                    inQ[v] = True
                    Q.append(v)

def find(v, f):
    if v == S: return f
    return find(prev[v], min(f, C[prev[v]][v] - F[prev[v]][v]))

def flow(v, f):
    if v == S: return
    total[0] += f * cost[prev[v]][v]
    F[prev[v]][v] += f
    F[v][prev[v]] -= f
    flow(prev[v], f)

while True:
    prev = [0] * N
    SPFA()
    if not prev[E]: break
    f = find(E, INF)
    flow(E, f)
print(-total[0])