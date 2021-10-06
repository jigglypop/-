import sys
sys.stdin = open("./text/9237.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
for i in range(N):
    nums[i] += i + 2
print(max(nums))