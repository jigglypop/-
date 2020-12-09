import sys
from pprint import pprint
from collections import Counter
sys.stdin = open('17298.txt', 'r')
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
S = [0]
result = [0] * N
for i in range(1, N):
    if not S:
        S.append(i)
    while S and nums[i] > nums[S[-1]]:
        result[S.pop()] = nums[i]
    S.append(i)
for i in range(N):
    if result[i] == 0:
        print(-1, end=" ")
    else:
        print(result[i], end=" ")
