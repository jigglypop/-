import sys
from pprint import pprint
from collections import deque
sys.stdin = open('17086.txt', 'r')
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
visited = [[-1] * X for _ in range(Y)]
Q = deque()
for y in range(Y):
    for x in range(X):
        if board[y][x] == 1:
            Q.append((y, x))
            visited[y][x] = 0

di = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
while Q:
    y, x = Q.popleft()
    for dy, dx in di:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if visited[ny][nx] == -1 and board[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                Q.append((ny, nx))
Max = 0
for y in range(Y):
    temp = max(visited[y])
    Max = max(Max, temp)
print(Max)
