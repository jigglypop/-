import sys
from pprint import pprint
sys.stdin = open("10709.txt", "r")

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
visited = [[-1 for _ in range(X)] for _ in range(Y)]
for y in range(Y):
    for x in range(X):
        if board[y][x] == 'c':
            i = 0
            _x = x
            while _x < X:
                visited[y][_x] = i
                i += 1
                _x += 1
for v in visited:
    print(' '.join(list(map(str, v))))
