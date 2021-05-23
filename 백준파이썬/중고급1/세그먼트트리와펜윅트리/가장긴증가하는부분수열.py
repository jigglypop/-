import sys
from bisect import bisect_left
sys.stdin = open("12015.txt", "r")
input = sys.stdin.readline

_ = int(input())
nums = list(map(int, input().split()))
S = []
for num in nums:
    if len(S) == 0:
        S.append(num)
    elif S[-1] < num:
        S.append(num)
    else:
        S[bisect_left(S, num)] = num
print(len(S))
