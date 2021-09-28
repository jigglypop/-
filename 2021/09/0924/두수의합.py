import sys
sys.stdin = open('./text/3273.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
X = int(input())
lo, hi = 0, len(nums) - 1
sums = 0
count = 0
while lo < hi:
    sums = nums[lo] + nums[hi]
    if sums < X:
        lo += 1
    else:
        if sums == X:
            count += 1
        hi -= 1
print(count)