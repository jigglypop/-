import sys
sys.setrecursionlimit(10000)
sys.stdin = open('2228.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
board = [0]+[int(input()) for _ in range(N)]
DP = [[None] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    board[i] += board[i-1]


def go(n, m):
    if m == 0:
        return 0
    if n <= 0:
        return -sys.maxsize
    if DP[n][m] is not None:
        return DP[n][m]
    DP[n][m] = go(n-1, m)
    for i in range(n, 0, -1):
        DP[n][m] = max(DP[n][m], board[n] - board[i-1] + go(i-2, m-1))
    return DP[n][m]


print(go(N, M))
