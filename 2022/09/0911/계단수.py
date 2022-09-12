from pprint import pprint
import sys
sys.stdin = open('./text/1562.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
mod = 1000000000
M = (1 << 10) - 1
dp = [[[0] * (M + 1) for _ in range(10)] for _ in range(N + 1)]
# i    j    k 
# 갯수  마지막 고른 숫자 
# [100][10][1024]
for j in range(1, 10):
    dp[1][j][1 << j] = 1
for i in range(2, N + 1):
    for j in range(10):
        for k in range(M + 1):
            if 1 <= j <= 9:
                dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
            if 0 <= j <= 8:
                dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]

result = 0
for j in range(10):
    result += dp[N][j][M]
print(result % mod)