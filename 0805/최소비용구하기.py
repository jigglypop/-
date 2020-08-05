import heapq
import sys
sys.stdin = open("최소비용구하기.txt", 'r')
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for point in graph[now]:
            cost = dist + point[1]
            if cost < distance[point[0]]:
                distance[point[0]] = cost
                heapq.heappush(q, (cost, point[0]))


dijkstra(start)
print(distance[end])
