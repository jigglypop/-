from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    heap = []
    distance[start] = 0
    heappush(q, (0, start))
    while heap:
        dist, new = heappop(q)
        if distance[new] < dist:
            continue
        for de, dc in graph[new]:
            cost = dist + dc
            if cost < distance[de]:
                distance[de] = cost
                heappush(q, (cost, de))
