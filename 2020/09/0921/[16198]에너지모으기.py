import sys
sys.stdin = open('16198.txt', 'r')

N = int(input())
nums = list(map(int, input().split()))
Max = 0


def perms(k, _nums, sums):
    global Max
    if len(_nums) == 2:
        Max = max(Max, sums)
        return
    for i in range(1, len(_nums)-1):
        temp = _nums[i-1] * _nums[i+1]
        perms(k,  _nums[:i] + _nums[i+1:], sums+temp)


perms(0, nums[::], 0)
print(Max)
