import sys
sys.stdin = open("LIS.txt", "r")

N = int(input())
S = [0] + list(map(int, input().split()))
DP = [0] * (N+1)
DP[1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        if S[i] > S[j]:
            DP[i] = max(DP[j], DP[i])
    DP[i] += 1
print(max(DP))
