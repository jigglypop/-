from heapq import heappop, heappush
import sys
sys.stdin = open("다익스트라.txt", "r")

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
    heappush(heap, (0, start))
    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heappush(heap, (cost, node[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
