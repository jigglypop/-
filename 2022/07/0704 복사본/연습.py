from pprint import pprint
import sys
sys.stdin = open("./text/2098.txt", "r")
input = sys.stdin.readline().strip()

dp = [-1] * 100
dp[0] = 0
dp[1] = 1

def go(x):
    if dp[x] != -1:
        return dp[x]
    dp[x] = go(x - 1) + go(x - 2)
    return dp[x]

print(go(10))
print(dp)
