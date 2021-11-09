from heapq import heappop, heappush
import sys
sys.stdin = open("./text/1715.txt", "r")
input = sys.stdin.readline
N = int(input())
Q = []
for _ in range(N):
    heappush(Q, int(input()))
if len(Q) == 1: 
    print(0)
else:
    result = 0
    while len(Q) > 1:
        a = heappop(Q) 
        b = heappop(Q) 
        result += a + b 
        heappush(Q, a + b) 
    print(result)