import sys
from pprint import pprint
sys.stdin = open('2228.txt', 'r')

N, M = map(int, input().split())
DP = [[[-sys.maxsize] * 2 for _ in range(M)] for _ in range(N)]
board = [int(input()) for _ in range(N)]
# DP[n][m][1]

Max = -sys.maxsize


def go(n, m, i):
    global Max
    if n <= N-1 and m == M:
        return board[n]
    if m > M:
        return 0
    if DP[n][m][i] != -sys.maxsize:
        return DP[n][m][i]
    DP[n][m][i] = 0
    if i == 1:
        DP[n][m][0] = max(go(n+1, m+1, 1) + board[n+1], go(n+1, m, 0))
        DP[n][m][1] = max(go(n+1, m, 1) + board[n+1], go(n+1, m, 0))
    else:
        DP[n][m][1] = max(go(n+1, m, 1) + board[n+1], go(n+1, m, 0))
        DP[n][m][0] = max(go(n+1, m+1, 1) + board[n+1], go(n+1, m, 0))
    return DP[n][m][i]


go(0, 0, 0)
print(Max)
pprint(DP)
