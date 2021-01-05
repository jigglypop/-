import sys
sys.stdin = open("15992.txt", "r")

DP = [[1 if i == 0 else 0]*1001 for i in range(1001)]
for i in range(1, 1001):
    for j in range(1, 1001):
        if i >= 1:
            DP[i][j] += DP[i-1][j-1]
        if i >= 2:
            DP[i][j] += DP[i-2][j-1]
        if i >= 3:
            DP[i][j] += DP[i-3][j-1]
        DP[i][j] %= 1000000009

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(DP[n][m])
