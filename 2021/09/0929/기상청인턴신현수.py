import sys
sys.stdin = open("./text/2435.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
nums = [0] + nums
Max = -201
for i in range(K, N + 1):
    Max = max(Max, nums[i] - nums[i - K])
print(Max)