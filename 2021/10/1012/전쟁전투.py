import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/1303.txt", "r")
input = sys.stdin.readline
X, Y = map(int, input().split())
board = [list(input().rstrip()) for _ in range(Y)]

def P(board):
    for b in board:
        print(b)
    print()

P(board)


def bfs(sy, sx, flag):
    di = ((-1, 0), (1, 0), (0, -1), (0, 1))
    Q = deque([(sy, sx)])
    board[sy][sx] = 'O'
    result = 0
    while Q:
        y, x = Q.popleft()
        result += 1
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] == flag:
                    board[ny][nx] = 'O'
                    Q.append((ny, nx))
    return result ** 2

W = 0
B = 0
for y in range(Y):
    for x in range(X):
        if board[y][x] == 'W':
            W += bfs(y, x, board[y][x])
        elif board[y][x] == 'B':
            B += bfs(y, x, board[y][x])
print(W, B)