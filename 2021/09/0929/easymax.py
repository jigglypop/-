import sys
from pprint import pprint
sys.stdin = open("./text/17203.txt", "r")
input = sys.stdin.readline
N, Q = map(int, input().split())
nums = list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(1, N):
    dp[i + 1] = abs(nums[i] - nums[i - 1]) + dp[i]
for _ in range(Q):
    a, b = map(int, input().split())
    print(dp[b] - dp[a])