import sys
from heapq import heappop, heappush
from collections import defaultdict
sys.stdin = open('1162.txt', 'r')

N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = defaultdict(list)
heap = [(0, 1)]
while heap:
    time, node = heappop(heap)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heappush(heap, (alt, v))
print(dist)
