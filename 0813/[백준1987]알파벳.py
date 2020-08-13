from collections import deque
import sys

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, ans):
    global answer
    answer = max(ans, answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in passed):
            passed.append(board[nx][ny])
            DFS(nx, ny, ans+1)
            passed.remove(board[nx][ny])


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
DFS(0, 0, answer)
print(answer)
