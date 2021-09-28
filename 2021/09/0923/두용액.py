import sys
sys.stdin = open('./text/2470.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums)
start, end = 0, len(nums) - 1
sums = abs(start + end)
print(sums)