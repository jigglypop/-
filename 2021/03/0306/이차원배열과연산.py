import sys
from pprint import pprint
from collections import Counter
sys.stdin = open("17140.txt", "r")


def rotate(board):
    Y = len(board)
    X = len(board[0])
    _board = [[0] * Y for _ in range(X)]
    for y in range(Y):
        for x in range(X):
            _board[x][y] = board[y][x]
    return _board


def make(board):
    Y = len(board)
    X = len(board[0])
    _board = []
    Max = 0
    for i in range(Y):
        temp = []
        for key, value in Counter(board[i]).items():
            if key == 0:
                continue
            temp.append([key, value])
        temp = sorted(temp, key=lambda x: (x[1], x[0]))
        temp = sum(temp, [])
        _board.append(temp)
        Max = max(Max, len(temp))
    for b in _board:
        L = Max - len(b)
        b += [0] * L
    return _board


y, x, k = map(int, input().split())
y -= 1
x -= 1
board = [list(map(int, input().split())) for _ in range(3)]
n = 0
result = -1
while n <= 100:
    Y = len(board)
    X = len(board[0])
    if 0 <= y < Y and 0 <= x < X:
        if board[y][x] == k:
            result = n
            break
    if Y >= X:
        board = make(board)
    else:
        board = rotate(board)
        board = make(board)
        board = rotate(board)
    n += 1
print(result)
