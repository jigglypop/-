import sys
from math import ceil
sys.stdin = open('./text/2792.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
colors = [int(input()) for _ in range(M)]
lo, hi = 0, max(colors)
while lo + 1 < hi:
    temp = 0
    mid = (lo + hi) // 2
    for color in colors:
        temp += ceil(color / mid)
    if temp > N:
        lo = mid
    else:
        hi = mid
print(hi)
