import sys
from heapq import heappop, heappush
sys.stdin = open("./text/1655.txt", "r")
N = int(input())
Q = []
Max = -10001
for _ in range(N):
    nums = int(input())
    if len(Q) == 0:
        print(1)
        heappush(Q, nums)
        continue
    temp = heappop(Q)
    heappush(Q, nums)
