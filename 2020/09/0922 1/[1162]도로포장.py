import sys
from heapq import heappop, heappush
from collections import defaultdict
sys.stdin = open('1162.txt', 'r')

N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = defaultdict(int)
heap = [(0, 1, K)]
while heap:
    time, node, k = heappop(heap)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heappush(heap, (alt, v, k))
            if k > 0:
                heappush(heap, (time, v, k-1))
print(dist)
