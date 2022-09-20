from copy import copy
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/2631.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
nums = [Int() for _ in range(N)]
dp = [1] * (N + 1)
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))