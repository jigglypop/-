from heapq import *
import sys
sys.stdin = open("./text/1655.txt", "r")
input = sys.stdin.readline
max_h, min_h = [], []
for i in range(int(input())):
    n = int(input())
    if len(max_h) == len(min_h):
        heappush(max_h, -n)
    else:
        heappush(min_h, n)

    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
        max_value = heappop(max_h) * -1
        min_value = heappop(min_h)
        
        heappush(max_h, min_value * -1)
        heappush(min_h, max_value)
    print(max_h[0] * -1)

    