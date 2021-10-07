import sys
sys.stdin = open("./text/12847.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
Max = 0
for i in range(1, n + 1):
    nums[i] += nums[i - 1]
for i in range(m, n + 1):
    Max = max(Max, nums[i] - nums[i - m])
print(Max)