import sys
from heapq import heappush, heappop
sys.stdin = open('1927.txt', 'r')

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, n)
