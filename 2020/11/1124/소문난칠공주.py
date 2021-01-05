import sys
from pprint import pprint
sys.stdin = open('1941.txt', 'r')

board = [list(input()) for _ in range(5)]
result = set()


def go(k, y, x, S, Y, choice):
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    if Y >= 4:
        return
    if k == 7:
        result.add(choice)
        print(choice)
        return
    for dy, dx in di:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 5 and 0 <= nx < 5:
            i = ny * 5 + nx + 1
            if not choice & (1 << i):
                if board[ny][nx] == 'S':
                    go(k+1, ny, nx, S+1, Y, choice | (1 << i))
                if board[ny][nx] == 'Y':
                    go(k+1, ny, nx, S, Y+1, choice | (1 << i))


for y in range(5):
    for x in range(5):
        go(0, y, x, 0, 0, 0)
print(result)
print(bin(1083328))
