import sys
from collections import deque
sys.stdin = open('2206.txt', 'r')

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
visited = [[[0] * 2 for _ in range(X)] for _ in range(Y)]


def BFS():
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    Q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while Q:
        y, x, crash = Q.popleft()
        if y == Y-1 and x == X-1:
            print(visited[y][x][crash])
            return
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if not visited[ny][nx][crash]:
                    if board[ny][nx] == '0':
                        visited[ny][nx][crash] = visited[y][x][crash] + 1
                        Q.append((ny, nx, crash))
                    if board[ny][nx] == '1' and crash == 0:
                        visited[ny][nx][1] = visited[y][x][crash] + 1
                        Q.append((ny, nx, 1))
    print(-1)
    return


BFS()
