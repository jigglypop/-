import sys
from heapq import heappop, heappush
sys.stdin = open('1162.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())
INF = sys.maxsize
dist = [[INF] * (K+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
heap = [(0, 1, 0)]
dist[1][0] = 0
while heap:
    time, u, k = heappop(heap)
    if dist[u][k] < time:
        continue
    for v, w in graph[u]:
        if k+1 <= K and dist[v][k+1] > time:
            dist[v][k+1] = time
            heappush(heap, (dist[v][k+1], v, k+1))
        if dist[v][k] > time + w:
            dist[v][k] = time + w
            heappush(heap, (dist[v][k], v, k))

print(min(dist[N]))
