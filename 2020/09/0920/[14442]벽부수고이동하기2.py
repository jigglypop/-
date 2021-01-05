import sys
from collections import deque
sys.stdin = open('14442.txt', 'r')

Y, X, K = map(int, input().split())
board = [list(input()) for _ in range(Y)]
visited = [[[0] * (K+1) for _ in range(X)] for _ in range(Y)]


def BFS():
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    Q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    while Q:
        y, x, k = Q.popleft()
        if y == Y-1 and x == X-1:
            print(visited[y][x][k])
            return
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if board[ny][nx] == '1' and k+1 <= K:
                    if visited[ny][nx][k+1] == 0:
                        visited[ny][nx][k+1] = visited[y][x][k] + 1
                        Q.append((ny, nx, k+1))
                if board[ny][nx] == '0':
                    if visited[ny][nx][k] == 0:
                        visited[ny][nx][k] = visited[y][x][k] + 1
                        Q.append((ny, nx, k))
    print(-1)
    return


BFS()
