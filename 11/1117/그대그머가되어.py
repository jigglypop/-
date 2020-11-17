import sys
from heapq import heappop, heappush
sys.stdin = open('14496.txt', 'r')
INF = sys.maxsize
input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append((1, y))
    graph[y].append((1, x))
heap = [(0, a)]
dist[a] = 0
while heap:
    cost, u = heappop(heap)
    if dist[u] < cost:
        continue
    for w, v in graph[u]:
        if dist[v] > dist[u] + 1:
            dist[v] = dist[u] + 1
            heappush(heap, (dist[v], v))

if dist[b] == INF:
    print(-1)
else:
    print(dist[b])
