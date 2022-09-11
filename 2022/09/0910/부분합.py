import sys
sys.stdin = open('./text/1806.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, S = Split()
nums = List()
l = r = 0
INF = sys.maxsize
result = INF
num = nums[r]
while r < N:
    if num < S:
        r += 1
        if r == N:break
        num += nums[r]
    else:
        num -= nums[l]
        result = min(result, r - l + 1)
        l += 1
print(result if result != INF else 0)
