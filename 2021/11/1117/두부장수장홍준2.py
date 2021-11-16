import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/11111.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
Y, X = map(int, input().split())
n = Y * X
N = 2 * n + 2
S, E = 1, 2 * n
total = [0]
board = [list(input().rstrip()) for _ in range(Y)]
graph = [[] * N for _ in range(N)]
C = [[0] * N for _ in range(N)]
F = [[0] * N for _ in range(N)]
cost = [[0] * N for _ in range(N)]
di = ((-1, 0), (0, -1), (1, 0), (0, 1))
table = [
    [10, 8, 7, 5, 1],
    [8, 6, 4, 3, 1],
    [7, 4, 3, 2, 1],
    [5, 3, 2, 2, 1],
    [1, 1, 1, 1, 0]]
alpha = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "F": 4
}

def P(board):
    for b in board:
        print(b)
    print()

def edge(a, b, f, w):
    C[a][b] = f
    cost[a][b] = w
    cost[b][a] = -w
    graph[a].append(b)
    graph[b].append(a)

for y in range(Y):
    for x in range(X):
        i = y * Y + x + 1
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                j = ny * Y + nx + 1
                if i < j:
                    a, b, c, d = 2 * i - 1, 2 * i, 2 * j - 1, 2 * j
                else:
                    a, b, c, d = 2 * j - 1, 2 * j , 2 * i -1, 2 * i
                A = alpha[board[y][x]]
                B = alpha[board[ny][nx]]
                w = table[A][B]
                edge(b, c, 1, w)
                edge(a, b, 1, 0)
                edge(c, d, 1, 0)
print(S, E)

while True:
    parent = [0] * N
    if not parent[E]: break
print(total[0])