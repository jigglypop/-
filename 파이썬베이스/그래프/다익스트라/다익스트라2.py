from heapq import heappop, heappush
import sys
sys.stdin = open("다익스트라.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dist = [INF] * (n + 1)


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        w, u = heappop(heap)
        if dist[u] < w:
            continue
        for v, dw in graph[u]:
            if dist[v] > w + dw:
                dist[v] = w + dw
                heappush(heap, (w + dw, v))


dijkstra(start)
for i in range(1, n+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
