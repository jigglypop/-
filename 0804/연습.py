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


print(graph)


def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    print(distance)
    print(heapq)
    print(q)
    while q:
        dist, now = heapq.heappop(q)
        print(dist, now)
# Dijkstra(start)


# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])
Dijkstra(start)
