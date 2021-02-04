import sys
from pprint import pprint
sys.stdin = open('2407.txt', 'r')

n, m = map(int, input().split())
DP = [[0] * (x+1) for x in range(n+1)]
DP[0][0] = 1
for y in range(1, n+1):
    DP[y][0] = 1
    for x in range(1, y):
        DP[y][x] = DP[y-1][x] + DP[y-1][x-1]
    DP[y][y] = 1
print(DP[n][m])
