import sys
sys.stdin = open("./text/2839.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

INF = sys.maxsize
N = Int()
dp = [INF] * (N + 1)
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(3, N + 1):
    if dp[i - 3] != INF:
        dp[i] = min(dp[i - 3] + 1, dp[i])
    if dp[i - 5] != INF:
        dp[i] = min(dp[i - 5] + 1, dp[i])
print(dp[N] if dp[N] != INF else -1)