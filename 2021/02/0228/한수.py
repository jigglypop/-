import sys
sys.stdin = open('1065.txt', 'r')
N = int(input())
nums = [0 for _ in range(1001)]
for i in range(1, 100):
    nums[i] += nums[i-1] + 1
for i in range(100, 1001):
    num = list(map(int, list(str(i))))
    plus = 0
    if num[0] - num[1] == num[1] - num[2]:
        plus = 1
    nums[i] += nums[i-1] + plus
print(nums[N])
