import sys
from pprint import pprint
sys.setrecursionlimit(1000*1000)
sys.stdin = open('1937.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
di = ((-1, 0), (1, 0), (0, -1), (0, 1))


def go(y, x):
    if DP[y][x] != 0:
        return DP[y][x]
    DP[y][x] = 1
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= nx < N and 0 <= ny < N:
            if board[y][x] < board[ny][nx]:
                DP[y][x] = max(DP[y][x], go(ny, nx) + 1)
    return DP[y][x]


Max = 0

for y in range(N):
    for x in range(N):
        Max = max(Max, go(y, x))
print(Max)
