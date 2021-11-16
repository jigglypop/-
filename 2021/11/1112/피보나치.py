import sys
from pprint import pprint
sys.stdin = open("./text/9009.txt", "r")
input = sys.stdin.readline
dp = [0] * 46
dp[0] = 1
dp[1] = 1
for i in range(2, 46):
    dp[i] = dp[i - 1] + dp[i - 2]
for j in range(int(input())):
    n = int(input())
    result = []
    while n:
        for k in range(46):
            if dp[k] <= n:
                t = dp[k]
        n -= t
        result.append(t)
        result.sort()
    for b in range(len(result)):
        print(result[b], end=' ')
    print()