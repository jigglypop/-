from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/15989.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)

N = Int()
nums = [Int() for _ in range(N)]
dp = [0] * (max(nums) + 1)
dp[0] = 1
for i in range(1, 4):
    for j in range(i, len(dp)):
        dp[j] += dp[j - i]
for num in nums:
    print(dp[num])
        