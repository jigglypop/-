def P(board):
    for b in board:
        print(b)
    print()

import sys
sys.stdin = open('14391.txt', 'r')
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, list(input().replace('\n', '')))) for _ in range(Y)]
for b in range(1 << Y * X):
    visited = [[0] * X for _ in range(Y)]
    for y in range(Y):
        for x in range(X):
            i = y * X + x
            if b & (1 << i):
                visited[y][x] = 1
    P(visited)
