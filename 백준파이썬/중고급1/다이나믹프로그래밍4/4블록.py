import sys
from pprint import pprint
sys.stdin = open("14389.txt", "r")


def isOn(state, row):
    return state & (1 << row) > 0


N, M = map(int, input().split())
_board = [list(input()) for _ in range(N)]
DP = [[0] * (1 << N) for _ in range(M)]
board = [[0] * N for _ in range(M)]
for y in range(M):
    for x in range(N):
        if _board[x][y] == '1':
            board[y][x] = 1

for row in range(M):
    for state in range(1 << N):
        print(DP[row][state], end=" ")
    print()
