import sys
sys.stdin = open('1328.txt', 'r')
input = sys.stdin.readline
DP = [[[0] * 101 for _ in range(101)] for _ in range(101)]
N, L, R = map(int, input().split())
mod = 1000000007
DP[1][1][1] = 1
for i in range(2, N+1):
    for j in range(1, L+1):
        for k in range(1, R+1):
            DP[i][j][k] = DP[i-1][j-1][k] + \
                DP[i-1][j][k-1] + DP[i-1][j][k] * (i-2)
            DP[i][j][k] %= mod
print(DP[N][L][R])
