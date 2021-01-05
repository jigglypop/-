import sys
from pprint import pprint
from collections import deque
sys.stdin = open('2589.txt', 'r')
Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
Max = 0


def bfs(sy, sx):
    global Max
    visited = [[0] * X for _ in range(Y)]
    visited[sy][sx] = 1
    Q = deque([(sy, sx)])
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while Q:
        y, x = Q.popleft()
        for dy, dx in di:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if visited[ny][nx] == 0 and board[ny][nx] == 'L':
                    Q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    Max = max(visited[ny][nx], Max)


for y in range(Y):
    for x in range(X):
        if board[y][x] == 'L':
            bfs(y, x)
print(Max - 1)
