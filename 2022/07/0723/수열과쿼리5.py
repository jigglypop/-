from math import sqrt
import sys
sys.stdin = open('./text/13547.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Tuple():return tuple(map(int, input().strip().split()))
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
MAX = 1000002

N = Int()
A = [0] + List()
M = Int()
query = [List() + [i] for i in range(M)]
sqrtN = int(N ** 0.5)
query.sort(key=lambda x: (x[0] // sqrtN, x[1]))
s, e, _i = query[0][0], query[0][1], query[0][2]
result = [0] * M
nums = [0] * MAX
count = 0

for i in range(s, e + 1):
    if nums[A[i]] == 0:count += 1
    nums[A[i]] += 1
result[_i] = count

for i in range(1, M):
    _s, _e, _i = query[i][0], query[i][1], query[i][2]
    while s < _s:
        nums[A[s]] -= 1
        if nums[A[s]] == 0:count -= 1
        s += 1
    while s > _s:
        s -= 1
        if nums[A[s]] == 0:count += 1
        nums[A[s]] += 1
    while e < _e:
        e += 1
        if nums[A[e]] == 0:count += 1
        nums[A[e]] += 1
    while e > _e:
        nums[A[e]] -= 1
        if nums[A[e]] == 0:count -= 1
        e -= 1
    result[_i] = count
print(*result, sep='\n')