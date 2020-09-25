import sys
from bisect import bisect_left
sys.stdin = open('14003.txt', 'r')
input = sys.stdin.readline

_ = input()
nums = list(map(int, input().split()))
lis_nums = [nums[0]]
res = [0]
for n in nums[1:]:
    if lis_nums[-1] < n:
        lis_nums.append(n)
        res.append(len(lis_nums)-1)
    else:
        where = bisect_left(lis_nums, n)
        lis_nums[where] = n
        res.append(where)

i = len(lis_nums)
print(i)
ans = []
for idx in range(len(res)-1, -1, -1):
    if res[idx] == i-1:
        ans.append(nums[idx])
        i -= 1
print(*ans[::-1])
