import sys
from pprint import pprint
sys.stdin = open('1080.txt', 'r')

Y, X = map(int, input().split())
before = [list(input()) for _ in range(Y)]
after = [list(input()) for _ in range(Y)]


def change(sy, sx, board):
    for y in range(sy, sy+3):
        for x in range(sx, sx+3):
            board[y][x] = '0' if board[y][x] == '1' else '1'
    return board


def isvalid(before):
    count = 0
    result = []
    for y in range(Y):
        for x in range(X):
            if y >= Y-2 or x >= X-2:
                result.append((y, x))
            else:
                if before[y][x] != after[y][x]:
                    count += 1
                    before = change(y, x, before)
    for ny, nx in result:
        if before[ny][nx] != after[ny][nx]:
            return -1
    return count


print(isvalid(before))
