import sys
sys.stdin = open('[백준2579]계단오르기.txt', 'r')
N = int(input())
m = []
for _ in range(N):
    m.append(int(input()))
DP = [0] * N
for i in range(N):
    if i == 0:
        DP[0] = m[0]
    elif i == 1:
        DP[1] = max(DP[i-1] + m[i], m[i])
    elif 1 < i <= 2:
        DP[i] = max(DP[i-2] + m[i], m[i-1] + m[i])
    else:
        DP[i] = max(DP[i-3] + m[i-1] + m[i], DP[i-2] + m[i])
print(DP[-1])
