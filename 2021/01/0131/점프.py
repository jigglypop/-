import sys
from pprint import pprint

sys.stdin = open('1890.txt', 'r')
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[-1] * N for _ in range(N)]


def go(y, x):
    if y == N-1 and x == N-1:
        return 1
    if DP[y][x] != -1:
        return DP[y][x]
    DP[y][x] = 0
    d = board[y][x]
    if 0 <= y + d < N:
        DP[y][x] += go(y + d, x)
    if 0 <= x + d < N:
        DP[y][x] += go(y, x + d)
    return DP[y][x]


print(go(0, 0))
