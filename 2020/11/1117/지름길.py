import sys
from heapq import heappop, heappush
sys.stdin = open('1446.txt', 'r')

input = sys.stdin.readline
N, D = map(int, input().split())
graph = [[(1, i+1)] for i in range(D+1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
INF = sys.maxsize
dist = [INF] * (D + 1)
heap = [(0, 0)]
dist[0] = 0
while heap:
    cost, u = heappop(heap)
    if dist[u] < cost:
        continue
    for w, v in graph[u]:
        if v > D:
            continue
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(heap, (dist[v], v))
print(dist[D])
