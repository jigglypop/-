import sys
from pprint import pprint
sys.stdin = open("./15990.txt", "r")
input = sys.stdin.readline
MAX = 1000000009
n = int(input())
nums = [int(input()) for _ in range(n)]
N = max(nums) + 1
dp = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
]
dp += [[0] * 4 for _ in range(4, N)]
for i in range(4, N):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MAX
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MAX
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MAX
for num in nums:
    print(sum(dp[num]) % MAX)