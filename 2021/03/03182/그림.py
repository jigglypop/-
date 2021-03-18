import sys
from collections import deque
from pprint import pprint
sys.stdin = open("1926.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
area = cnt = 0
for y in range(Y):
    for x in range(X):
        if board[y][x] == 1:
            Q = deque([(y, x)])
            board[y][x] = 0
            count = 1
            while Q:
                sy, sx = Q.popleft()
                for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ny, nx = sy + dy, sx + dx
                    if 0 <= ny < Y and 0 <= nx < X:
                        if board[ny][nx] == 1:
                            board[ny][nx] = 0
                            count += 1
                            Q.append((ny, nx))
            area = max(area, count)
            cnt += 1

print(cnt)
print(area)
