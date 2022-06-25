import sys
sys.stdin = open("./text/2098.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0
for state in range(1 << N):
    for i in range(1, N):
        if state & (1 << i):
            for j in range(N):
                if i != j and state & (1 << j) and A[j][i] != 0:
                    dp[state][i] = min(dp[state][j], dp[state - (1 << i)][j] + A[j][i]) 
result = INF
for i in range(N):
    if A[i][0] != 0:
        result = min(result, dp[(1 << N) - 1][i] + A[i][0])
print(result)