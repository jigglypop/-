import sys
from heapq import heappop, heappush
sys.stdin = open("1753.txt", "r")
input = sys.stdin.readline
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
    if w > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(Q, (dist[v], v))

dist = list(map(lambda x: "INF" if x == INF else x, dist))[1:]
for d in dist:
    print(d)
