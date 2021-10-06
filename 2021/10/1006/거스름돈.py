import sys
sys.stdin = open("./text/14916.txt", "r")
input = sys.stdin.readline
N = int(input())

if N == 2 or N == 5:
    print(1)
elif N == 4:
    print(2)
elif N < 5:
    print(-1)
else:
    dp = [-1] * (N + 1)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, N + 1):
        temp = []
        if dp[i - 2] != -1:
            temp.append(dp[i - 2] + 1)
        if dp[i - 5] != -1:
            temp.append(dp[i - 5] + 1)
        if len(temp) >= 1:
            dp[i] = min(temp)
        else:
            dp[i] = -1
    print(dp[N])
