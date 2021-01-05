import sys
INF = sys.maxsize
sys.stdin = open('12869.txt', 'r')
input = sys.stdin.readline


def go(i, j, k):
    if i == j == k == 0:
        return 0

    if dp[i][j][k] != -1:
        return dp[i][j][k]

    dp[i][j][k] = min(
        go(max(0, i-1), max(0, j-3), max(0, k-9)),
        go(max(0, i-1), max(0, j-9), max(0, k-3)),
        go(max(0, i-3), max(0, j-1), max(0, k-9)),
        go(max(0, i-3), max(0, j-9), max(0, k-1)),
        go(max(0, i-9), max(0, j-1), max(0, k-3)),
        go(max(0, i-9), max(0, j-3), max(0, k-1)),
    ) + 1
    return dp[i][j][k]


n = int(input())
a, b, c = [*map(int, input().split())] + [0]*(3-n)
dp = [[[-1]*61 for i in range(61)] for j in range(61)]
print(go(a, b, c))
