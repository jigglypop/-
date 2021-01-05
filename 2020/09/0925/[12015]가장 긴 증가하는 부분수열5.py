import sys
from bisect import bisect_left
sys.stdin = open('14003.txt', 'r')
input = sys.stdin.readline

_ = int(input())
nums = list(map(int, input().split()))
S = [nums[0]]
result = [0]
for num in nums[1:]:
    if S[-1] < num:
        S.append(num)
        result.append(len(S) - 1)
    else:
        S[bisect_left(S, num)] = num
        result.append(bisect_left(S, num))
i = len(S)
print(i)
ans = []
for idx in range(len(result)-1, -1, -1):
    if result[idx] == i-1:
        ans.append(nums[idx])
        i -= 1
print(*ans[::-1])
