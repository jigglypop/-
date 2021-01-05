import sys
from heapq import heappush, heappop
sys.stdin = open('11279.txt', 'r')

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -n)
