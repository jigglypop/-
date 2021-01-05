import sys
from heapq import heappop, heappush
sys.stdin = open('5972.txt', 'r')

input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dist = [INF for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
heap = [(0, 1)]
dist[1] = 0
while heap:
    u = heappop(heap)
    for cost, v in graph[u[1]]:
        if dist[v] < cost:
            continue
        if dist[v] > dist[u[1]] + cost:
            dist[v] = dist[u[1]] + cost
            heappush(heap, (dist[v], v))
print(dist[N])
