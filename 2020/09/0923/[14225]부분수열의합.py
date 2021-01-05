import sys
sys.stdin = open('14225.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
sums = 0
result = sum(nums) + 1
for num in nums:
    if sums < num-1:
        result = sums+1
        break
    sums += num
print(result)
