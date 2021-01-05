import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open('1766.txt', 'r')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    check[b] += 1
heap = []
for i in range(1, len(check)):
    if check[i] == 0:
        heappush(heap, i)
# result = []
while heap:
    u = heappop(heap)
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            heappush(heap, v)
    print(u, end=' ')
