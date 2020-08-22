import sys
import heapq
sys.stdin = open("다익스트라.txt")
INF = (1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def Dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for point in graph[now]:
            cost = dist + point[1]
            if cost < distance[point[0]]:
                distance[point[0]] = cost
                heapq.heappush(q, (cost, point[0]))


Dijkstra(start)
print(distance)
