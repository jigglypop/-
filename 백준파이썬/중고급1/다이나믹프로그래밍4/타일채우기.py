import sys
# input = sys.stdin.readline
input = open('./2133.txt').readline
N = int(input())
DP = [[0 for _ in range(8)] for _ in range(N + 1)]
DP[0][7] = 1
for i in range(1, N+1):
    DP[i][0] = DP[i-1][7]
    DP[i][1] = DP[i-1][6]
    DP[i][2] = DP[i-1][5]
    DP[i][4] = DP[i-1][3]
    DP[i][3] = DP[i-1][4] + DP[i-1][7]
    DP[i][6] = DP[i-1][1] + DP[i-1][7]
    DP[i][5] = DP[i-1][2]
    DP[i][7] = DP[i-1][0] + DP[i-1][3] + DP[i-1][6]
print(DP[N][7])
