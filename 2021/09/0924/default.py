import sys
sys.stdin = open('./text/6159.txt', 'r')
N, S = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
lo, hi = 0, len(nums) - 1
count = 0
while lo < hi:
    sums = nums[lo] + nums[hi]
    if sums <= S:
        count += 1
        print(sums)
        lo += 1
    else:
        hi -= 1
print(count)