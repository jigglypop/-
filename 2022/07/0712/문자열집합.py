from heapq import heappop, heappush
import sys
from math import *
sys.stdin = open('./text/14425.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N, M = Split()
A = set([input().strip() for _ in range(N)])
B = [input().strip() for _ in range(M)]
result = 0
for b in B:
    if b in A:
        result += 1
print(result)