import sys
sys.stdin = open('1648.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
DP = [[0]*(1 << m) for i in range(n*m+1)]
DP[n*m][0] = 1
for i in range(n*m-1, -1, -1):
    for j in range(1 << m):
        if j & 1:
            DP[i][j] = DP[i+1][j >> 1]
            continue
        if i < (n-1)*m:
            DP[i][j] += DP[i+1][(1 << (m-1)) | (j >> 1)]
        if i % m < m-1 and not j % 4:
            DP[i][j] += DP[i+2][j >> 2]
print(DP[0][0] % 9901)
