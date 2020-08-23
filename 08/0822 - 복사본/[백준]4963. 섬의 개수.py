from collections import deque
from pprint import pprint
import sys
sys.stdin = open('4963.txt', 'r')


def DFS(board, sy, sx, Y, X):
    stack = deque([(sy, sx)])
    di = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))
    while stack:
        y, x = stack.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X and board[ny][nx] == 1:
                board[ny][nx] = 0
                stack.append((ny, nx))
    return board


while True:
    X, Y = map(int, input().split())
    if X == Y == 0:
        break
    board = []
    for _ in range(Y):
        board.append(list(map(int, input().split())))
    result = 0
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 1:
                result += 1
                board = DFS(board, y, x, Y, X)
    print(result)
