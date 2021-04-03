import sys
sys.stdin = open('2248.txt', 'r')
N, L, K = map(int, input().split())
DP = [[0] * 32 for _ in range(32)]
for i in range(31):
    DP[0][i] = 1
for i in range(1, 32):
    DP[i][0] = DP[i-1][0]
    for j in range(1, 32):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
while N > 0:
    if K <= DP[N-1][L]:
        print('0', end="")
        N -= 1
    else:
        print('1', end="")
        K -= DP[N-1][L]
        N -= 1
        L -= 1
