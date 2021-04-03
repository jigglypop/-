import sys
# input = sys.stdin.readline
input = open('./2098.txt').readline
INF = sys.maxsize
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0
for i in range(1 << N):
    for j in range(1, N):
        if i & (1 << j) != 0:
            for k in range(N):
                if k != j and i & (1 << k) != 0 and A[k][j] != 0:
                    dp[i][j] = min(dp[i][j], dp[i - (1 << j)][k] + A[k][j])
result = INF
for i in range(N):
    if A[i][0] != 0:
        result = min(result, dp[(1 << N) - 1][i] + A[i][0])
print(result)
