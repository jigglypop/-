import sys
from heapq import heappop, heappush
INF = sys.maxsize

sys.stdin = open('14284.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
s, e = map(int, input().split())
heap = [(0, s)]
dist[s] = 0
while heap:
    u = heappop(heap)
    for cost, v in graph[u[1]]:
        if dist[v] < cost:
            continue
        if dist[v] > dist[u[1]] + cost:
            dist[v] = dist[u[1]] + cost
            heappush(heap, (dist[v], v))
print(dist[e])
