import sys
from pprint import pprint
sys.stdin = open("./text/15904.txt", "r")
input = sys.stdin.readline
Y = input()
X = "UCPC"
dp = [[0] * 5 for _ in range(len(Y) + 1)]
for y in range(1, len(Y) + 1):
    for x in range(1, 5):
        if Y[y-1] == X[x-1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
result = "I"
result += " love" if dp[len(Y)][4] == 4 else " hate"
result += " UCPC"
print(result)