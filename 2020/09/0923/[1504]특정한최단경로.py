from heapq import heappush, heappop
from sys import stdin
stdin = open('1504.txt', 'r')
input = stdin.readline
INF = 1e9
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())


def dijkstra(s, e):
    dist = [INF] * (n+1)
    heap = [(0, s)]
    dist[s] = 0
    while heap:
        time, node = heappop(heap)
        if dist[node] < time:
            continue
        for v, w in graph[node]:
            alt = time + w
            if dist[v] > alt:
                dist[v] = alt
                heappush(heap, (alt, v))
    return dist[e]


path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
result = min(path1, path2)
print(result if result < INF else "-1")
