import sys
from copy import deepcopy
from collections import deque
from pprint import pprint

def P(board):
    for b in board:
        print(b)

sys.stdin = open("./text/14246.txt", "r")
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
k = int(input())
j = sums = count = 0
for i in range(n):
    while sums <= k and j < n:
        sums += nums[j]
        j += 1
    if sums > k:
        count += n - j + 1
    sums -= nums[i]
print(count)
