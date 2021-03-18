import sys
from copy import deepcopy
from pprint import pprint
sys.stdin = open("16935.txt", "r")
Y, X, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
orders = list(map(int, input().split()))


def make(order):
    global board
    Y = len(board)
    X = len(board[0])
    if order == 1:
        board = board[::-1]
    elif order == 2:
        board = list(map(lambda b: b[::-1], board))
    elif order == 3:

        _board = [[0] * Y for _ in range(X)]
        for y in range(Y):
            for x in range(X):
                _board[x][Y-y-1] = board[y][x]
        board = _board
    elif order == 4:
        _board = [[0] * Y for _ in range(X)]
        for y in range(Y):
            for x in range(X):
                _board[X-x-1][y] = board[y][x]
        board = _board
    elif order == 5:
        _board = [[0] * X for _ in range(Y)]
        _Y = Y // 2
        _X = X // 2
        for y in range(_Y):
            for x in range(_X):
                _board[y][_X+x] = board[y][x]
        for y in range(_Y):
            for x in range(_X, X):
                _board[_Y+y][x] = board[y][x]
        for y in range(_Y, Y):
            for x in range(_X, X):
                _board[y][x-_X] = board[y][x]
        for y in range(_Y, Y):
            for x in range(_X):
                _board[y-_Y][x] = board[y][x]
        for y in range(Y):
            for x in range(X):
                board[y][x] = _board[y][x]
    else:
        _board = [[0] * X for _ in range(Y)]
        _Y = Y // 2
        _X = X // 2
        for y in range(_Y):
            for x in range(_X):
                _board[y-_Y][x] = board[y][x]
        for y in range(_Y, Y):
            for x in range(_X):
                _board[y][_X+x] = board[y][x]
        for y in range(_Y, Y):
            for x in range(_X, X):
                _board[y - _Y][x] = board[y][x]
        for y in range(Y):
            for x in range(_X, X):
                _board[y][x-_X] = board[y][x]

        for y in range(Y):
            for x in range(X):
                board[y][x] = _board[y][x]


for order in orders:
    make(order)

list(map(lambda b: print(*b), board))
