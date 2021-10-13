import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/21736.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(input().rstrip()) for _ in range(Y)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
Q = deque()
visited = [[False] * X for _ in range(Y)]

for y in range(Y):
    for x in range(X):
        if board[y][x] == 'I':
            Q.append((y, x))
            visited[y][x] = True
P = []
while Q:
    y, x = Q.popleft()
    if board[y][x] == 'P':
        P.append((y, x))
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < Y and 0 <= nx < X:
            if not visited[ny][nx] and board[ny][nx] != 'X':
                Q.append((ny, nx))
                visited[ny][nx] = True
print(len(P) if len(P) >= 1 else 'TT')

    