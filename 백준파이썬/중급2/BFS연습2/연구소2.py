import sys
from copy import deepcopy
from collections import deque
from pprint import pprint
from itertools import combinations
sys.stdin = open("17141.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Y = len(board)
X = len(board[0])
zero = 0
two = []
_board = [[0] * X for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        if board[y][x] == 2:
            two.append([y, x])
        elif board[y][x] == 0:
            _board[y][x] = 0
            zero += 1
        else:
            _board[y][x] = 1
orders = list(combinations([i for i in range(len(two))], M))


def bfs(order):
    maps = deepcopy(_board)
    Q = deque()
    visited = [[-1] * X for _ in range(Y)]
    for i in order:
        sy, sx = two[i]
        Q.append([sy, sx])
        visited[sy][sx] = 0
        maps[sy][sx] = 2
    while Q:
        y, x = Q.popleft()
        for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if visited[ny][nx] == -1 and maps[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    Q.append([ny, nx])
    Max = -1
    for y in range(Y):
        for x in range(X):
            if maps[y][x] == 0 or maps[y][x] == 2:
                if visited[y][x] == -1:
                    return -1
                else:
                    Max = max(Max, visited[y][x])
    return Max


Min = sys.maxsize
for order in orders:
    temp = bfs(order)
    if temp != -1:
        Min = min(bfs(order), Min)
print(Min if Min != sys.maxsize else -1)
