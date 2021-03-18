import sys
from heapq import heappop, heappush
from collections import defaultdict
sys.stdin = open("다익스트라.txt", "r")

V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = defaultdict(int)
heap = [(0, start)]
while heap:
    time, node = heappop(heap)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heappush(heap, (alt, v))
print(dist)
print(graph)
