import sys
sys.stdin = open("설탕배달.txt", 'r')
input = sys.stdin.readline

N = int(input())


def DP(N):
    dp = [-1] * (N+1)
    if N >= 3:
        dp[3] = 1
    if N >= 5:
        dp[5] = 1
    if N < 6:
        return dp[N]
    else:
        for i in range(6, N+1):
            if dp[i-3] < 0 and dp[i-5] < 0:
                dp[i] = -1
            elif dp[i-3] < 0 and dp[i-5] > 0:
                dp[i] = dp[i-5] + 1
            elif dp[i-3] > 0 and dp[i-5] < 0:
                dp[i] = dp[i-3] + 1
            else:
                dp[i] = min(dp[i-3], dp[i-5]) + 1
    return dp[N]


print(DP(N))
