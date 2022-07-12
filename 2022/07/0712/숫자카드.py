from heapq import heappop, heappush
import sys
from math import *
sys.stdin = open('./text/10815.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N = Int()
A = set(Split())
M = Int()
B = list(Split())
for b in B:
    if b in A:
        print(1, end=" ")
    else:
        print(0, end=" ")