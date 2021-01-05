from collections import deque
from pprint import pprint
import sys
sys.stdin = open("16954.txt", "r")
temp = [list(input()) for _ in range(8)] + [['.'] * 8 for _ in range(8)]
boards = []
for i in range(8):
    Q = deque(temp)
    Q.rotate(i)
    t = []
    for _ in range(8):
        t.append(Q.popleft())
    boards.append(t)


def bfs():
    visited = [[[False] * 8 for _ in range(8)] for _ in range(8)]
    Q = deque()
    visited[7][0][0] = True
    Q.append((7, 0, 0))
    di = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (1, 1))
    while Q:
        y, x, s = Q.popleft()
        if boards[y][x][s] == '#':
            continue
        print(y, x, s)
        if s == 7:
            return 1
        for dy, dx in di:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if boards[ny][nx][s+1] == '.' and not visited[ny][nx][s+1]:
                    visited[ny][nx][s] = True
                    Q.append((ny, nx, s+1))

    return 0


print(bfs())
