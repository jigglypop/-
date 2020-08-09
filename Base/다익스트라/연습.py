from heapq import heappop, heappush
import sys
sys.stdin = open("다익스트라.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
start = int(input())
graph = [[] for i in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])

heap = []
distance = [INF for _ in range(V+1)]
distance[start] = 0
heappush(heap, (0, start))

while heap:
    mid = heappop(heap)
    for end in graph[mid[1]]:
        if distance[end[0]] > mid[0] + end[1]:
            distance[end[0]] = mid[0] + end[1]
            heappush(heap, (distance[end[0]], end[0]))

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
