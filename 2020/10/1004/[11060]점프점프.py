import sys
sys.stdin = open('11060.txt', 'r')
INF = sys.maxsize
N = int(input())
A = list(map(int, input().split()))
DP = [INF] * N
DP[0] = 0
for i in range(N):
    for j in range(i+1, min(i+A[i]+1, N)):
        DP[j] = min(DP[j], DP[i]+1)

print(DP[-1] if DP[-1] != INF else -1)
