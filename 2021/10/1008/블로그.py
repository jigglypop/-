import sys
sys.stdin = open("./text/21921.txt")
N, X = map(int, input().split())
nums = list(map(int, input().split()))
if max(nums) == 0:
    print("SAD")
else:
    max_nums = sum(nums[0:X])
    value = max_nums
    count = 1
    for i in range(X, N):
        value -= nums[i - X]
        value += nums[i]
        if value > max_nums:
            max_nums = value
            count = 1
        elif value == max_nums:
            count += 1
    print(max_nums)
    print(count)