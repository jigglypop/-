import sys
sys.stdin = open('./text/2217.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

nums = [Int() for _ in range(Int())]
nums.sort(reverse=True)
Max = 0
for i in range(len(nums)):
    Max = max(Max, nums[i] * (i + 1))
print(Max)
