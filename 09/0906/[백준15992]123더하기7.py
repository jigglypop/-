import sys
sys.stdin = open("15992.txt", "r")

DP = [[0]*1001 for i in range(1001)]
DP[0][0] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        DP[i][j] += DP[i-1][j-1]
        if i >= 2:
            DP[i][j] += DP[i-2][j-1]
        if i >= 3:
            DP[i][j] += DP[i-3][j-1]
        DP[i][j] %= 1000000009

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(DP[n][m])
