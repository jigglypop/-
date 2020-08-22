from collections import deque
from pprint import pprint
import sys
sys.stdin = open('13459.txt', 'r')

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]


visited = [[[[False] * X for _ in range(Y)]
            for _ in range(X)] for _ in range(Y)]


def move(y, x, dy, dx):
    count = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        count = 1
    return y, x, count


def BFS():
    di = ((1, 0), (-1, 0), (0, 1), (0, -1))
    Q = deque()
    ry, rx, by, bx = [0] * 4
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 'R':
                ry, rx = y, x
            elif board[y][x] == 'B':
                by, bx = y, x
    Q.append((ry, rx, by, bx, 1))
    visited[ry][rx][by][bx] = True

    while Q:
        ry, rx, by, bx, depth = Q.popleft()
        if depth > 10:
            break
        for dy, dx in di:
            nry, nrx, rc = move(ry, rx, dy, dx)
            nby, nbx, bc = move(by, bx, dy, dx)
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                print(1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                Q.append((nry, nrx, nby, nbx, depth + 1))
    print(0)


BFS()
