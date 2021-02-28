from collections import deque
import sys
from copy import deepcopy
from pprint import pprint
sys.stdin = open('16918.txt', 'r')
input = sys.stdin.readline


def loc_bombs():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bombs.append((i, j))


def make_bombs():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode():
    while bombs:
        r, c = bombs.popleft()
        board[r][c] = '.'
        if 0 <= r - 1:
            board[r - 1][c] = '.'
        if r + 1 < R:
            board[r + 1][c] = '.'
        if 0 <= c - 1:
            board[r][c - 1] = '.'
        if c + 1 < C:
            board[r][c + 1] = '.'


R, C, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
N -= 1
while N:
    bombs = deque()
    loc_bombs()
    make_bombs()
    N -= 1
    if N == 0:
        break
    explode()
    N -= 1
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()
