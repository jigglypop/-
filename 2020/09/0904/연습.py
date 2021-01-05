import sys
from collections import deque

sys.stdin = open("13460.txt", "r")

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
visited = [[[[False] * X for _ in range(Y)]
            for _ in range(X)] for _ in range(Y)]

di = ((-1, 0), (1, 0), (0, 1), (0, -1))
Q = deque()


def go(y, x, dy, dx):
    count = 0
    while board[y + dy][x+dx] != "#" and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1
    return y, x, count


for y in range(Y):
    for x in range(X):
        if board[y][x] == 'R':
            ry, rx = y, x
        elif board[y][x] == "B":
            by, bx = y, x
Q.append((ry, rx, by, bx, 1))
visited[ry][rx][by][bx] = True
result = -1
while Q:
    ry, rx, by, bx, depth = Q.popleft()
    if depth > 10:
        break
    for dy, dx in di:
        nry, nrx, rc = go(ry, rx, dy, dx)
        nby, nbx, bc = go(by, bx, dy, dx)
        if board[nby][nbx] == "O":
            continue
        if board[nry][nrx] == "O":
            result = depth if result == -1 else min(depth, result)
            break
        if nry == nby and nrx == nbx:
            if rc > bc:
                nry -= dy
                nrx -= dx
            else:
                nby -= dy
                nbx -= dx
        if not visited[nry][nrx][nby][nbx]:
            visited[nry][nrx][nby][nbx] = True
            Q.append((nry, nrx, nby, nbx, depth+1))
print(result)
