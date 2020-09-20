import sys
from collections import deque
sys.stdin = open('16933.txt', 'r')

Y, X, K = map(int, input().split())
board = [list(input()) for _ in range(Y)]
visited = [[[[0]*2 for _ in range(K+1)] for _ in range(X)] for _ in range(Y)]


def BFS():
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    Q = deque([(0, 0, 0, 0)])
    visited[0][0][0][0] = 1
    while Q:
        y, x, k, n = Q.popleft()
        if y == Y-1 and x == X-1:
            print(visited[y][x][k][n])
            return
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if n == 0:
                    if board[ny][nx] == '0':
                        if visited[ny][nx][k][1] == 0:
                            visited[ny][nx][k][1] = visited[y][x][k][n] + 1
                            Q.append((ny, nx, k, 1))
                    if board[ny][nx] == '1' and k+1 <= K:
                        if visited[ny][nx][k+1][1] == 0:
                            visited[ny][nx][k+1][1] = visited[y][x][k][n] + 1
                            Q.append((ny, nx, k+1, 1))
                    visited[y][x][k][1] = visited[y][x][k][n] + 1
                    Q.append((y, x, k, 1))
                if n == 1:
                    if board[ny][nx] == '0':
                        if visited[ny][nx][k][0] == 0:
                            visited[ny][nx][k][0] = visited[y][x][k][n] + 1
                            Q.append((ny, nx, k, 0))
                    visited[y][x][k][0] = visited[y][x][k][n] + 1
                    Q.append((y, x, k, 0))

    print(-1)
    return


BFS()
