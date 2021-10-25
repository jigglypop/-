import sys
sys.stdin = open("./10826.txt", "r")
N = int(input())
dp = [0, 1, 1]
dp += [0 for _ in range(3, N + 1)]
for i in range(3, N + 1):
    dp[i] += dp[i - 1] + dp[i - 2]
print(dp[N])