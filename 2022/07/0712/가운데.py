from heapq import heappop, heappush
import sys
from math import *
sys.stdin = open('./text/1655.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
L = []
R = []
for i in range(Int()):
    n = Int()
    if len(L) == len(R):
        heappush(L, -n)
    else:
        heappush(R, n)
    if R and R[0] < -L[0]:
        l = heappop(L)
        r = heappop(R)
        heappush(L, -r)
        heappush(R, -l)
    print(-L[0])