import sys
from heapq import heappop, heappush
sys.stdin = open("1753.txt", "r")
INF = sys.maxsize
V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
Q = [(0, S)]
dist = [INF] * (V + 1)
dist[S] = 0
while Q:
    w, u = heappop(Q)
    if dist[u] < w:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(Q, (dist[v], v))
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
