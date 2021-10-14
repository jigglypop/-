import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/14716.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]

def P(board):
    for b in board:
        print(b)
    print()

def bfs(sy, sx):
    Q = deque([(sy, sx)])
    di = ((-1, 0), (1, 0), (0, 1), (0, -1),
        (-1, -1), (1, 1), (-1, 1), (1, -1))
    board[sy][sx] = 1
    while Q:
        y, x = Q.popleft()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] == 1:
                    Q.append((ny, nx))
                    board[ny][nx] = 0

result = 0
for y in range(Y):
    for x in range(X):
        if board[y][x] == 1:
            result += 1
            bfs(y, x)
print(result)