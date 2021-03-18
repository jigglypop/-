import sys
sys.stdin = open('3273.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
result = 0
left = 0
right = N-1

while left < right:
    if nums[left] + nums[right] >= M:
        if nums[left] + nums[right] == M:
            result += 1
        right -= 1
    if nums[left] + nums[right] < M:
        left += 1
print(result)
