import sys
from pprint import pprint
from collections import Counter
sys.stdin = open('17299.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)

S = [0]
result = [0] * N
for i in range(1, N):
    if not S:
        S.append(i)
    while S and counter[nums[i]] > counter[nums[S[-1]]]:
        result[S.pop()] = nums[i]
    S.append(i)

for i in range(len(result)):
    if result[i] == 0:
        result[i] = -1
print(*result)
