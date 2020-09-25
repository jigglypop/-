import sys
sys.stdin = open('13397.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0,  max(nums)
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    Max = Min = nums[0]
    for num in nums[1:]:
        Max = max(num, Max)
        Min = min(num, Min)
        temp = Max - Min
        if temp > mid:
            Max = num
            Min = num
            count += 1
    if count > M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)
