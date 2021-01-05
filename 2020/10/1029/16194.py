import sys
sys.stdin = open("16194.txt", "r")
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(N+1):
    dp[i] = P[i]
for i in range(2, N+1):
    for j in range(N):
        if i - j >= 1:
            dp[i] = min(dp[i],  dp[i-j] + P[j])
print(dp[-1])
