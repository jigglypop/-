import sys
from copy import deepcopy
input = sys.stdin.readline
sys.stdin = open('2636.txt', 'r')
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
wrapper = []
count = 0
for y in range(Y):
    for x in range(X):
        if y == 0 or x == 0 or y == Y-1 or x == X-1:
            wrapper.append([y, x])
        if board[y][x] == 1:
            count += 1
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
n = 1
result = 0
while True:
    c = set()
    _board = deepcopy(board)
    for sy, sx in wrapper:
        if _board[sy][sx] == 0:
            S = [(sy, sx)]
            while S:
                y, x = S.pop()
                for dy, dx in di:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if _board[ny][nx] == 0:
                            _board[ny][nx] = 2
                            S.append([ny, nx])
                        if _board[ny][nx] == 1:
                            c.add((ny, nx))
    C = list(c)
    count -= len(C)
    if count <= 0:
        result = len(C)
        break
    for cy, cx in C:
        board[cy][cx] = 0
    n += 1
print(n)
print(result)
