import sys
sys.stdin = open('./text/3273.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
nums = List()
nums.sort()
M = Int()
r = N - 1
l = result = 0
while l < r:
    num = nums[l] + nums[r]
    if num > M:
        r -= 1
    elif num < M:
        l += 1
    else:
        result += 1
        l += 1
print(result)
