from copy import copy, deepcopy
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1202.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M = Split()
A = []
for _ in range(N):
    heappush(A, List())
B = [Int() for _ in range(M)]
B.sort()
result = 0
_A = []
for b in B:
    while A and b >= A[0][0]:
        heappush(_A, -heappop(A)[1])
    if _A:
        result -= heappop(_A)
    elif not A:
        break
print(result)