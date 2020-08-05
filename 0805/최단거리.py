import heapq
import sys
sys.stdin = open('최단거리.txt', 'r')

INF = (1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

visited = [False]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, new = heapq.heappop(q)
        if distance[new] < dist:
            continue
        for point in graph[new]:
            cost = dist + point[1]
            if cost < distance[point[0]]:
                distance[point[0]] = cost
                heapq.heappush(q, (cost, point[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
