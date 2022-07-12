from heapq import heappop, heappush
import sys
from math import *
sys.stdin = open('./text/11279.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

Q = []
for _ in range(Int()):
    n = Int()
    if n == 0:
        print(0) if len(Q) == 0 else print(-heappop(Q))
    else:
        heappush(Q, -n)
