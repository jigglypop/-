import sys
from collections import deque
sys.stdin = open('3055.txt', 'r')

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]

for y in range(Y):
    for x in range(X):
        if board[y][x] == 'D':
            D = (y, x)
        if board[y][x] == 'S':
            S = (y, x)

visited = [[0] * X for _ in range(Y)]
