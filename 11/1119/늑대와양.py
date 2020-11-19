import sys
from pprint import pprint
from collections import deque
sys.stdin = open("16956.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(input().rstrip()) for _ in range(Y)]


def bfs():
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 'W':
                for dy, dx in di:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if board[ny][nx] == 'S':
                            print(0)
                            return
            elif board[y][x] != 'S':
                board[y][x] = 'D'

    print(1)
    for b in board:
        for x in b:
            print(x, end='')
        print()
    return


bfs()
