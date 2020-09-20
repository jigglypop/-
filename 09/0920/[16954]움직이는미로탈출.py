import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('16954.txt', 'r')

temp = [list(input()) for _ in range(8)]
board = [deepcopy(temp) for _ in range(10)]
for i in range(8):
    for x in range(8):
        board[i+1][i][x] = '#'
visited = [[[False for _ in range(8)] for _ in range(8)] for _ in range(10)]


def BFS():
    di = ((-1, 0), (1, 0), (0, -1), (0, 1), (0, 0),
          (-1, 1), (1, 1), (-1, 1), (1, -1))
    Q = deque([(0, 7, 7)])
    visited[0][7][7] = True
    while Q:
        second, y, x = Q.popleft()
        if y == 0 and x == 0:
            print(1)
            return
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 8 and 0 <= nx < 8:
                if second >= 9:
                    _next = 9
                else:
                    _next = second + 1
                if not visited[_next][ny][nx] and board[_next][ny][nx] != '#':
                    visited[_next][ny][nx] = True
                    Q.append((_next, ny, nx))
    print(0)
    return


BFS()
