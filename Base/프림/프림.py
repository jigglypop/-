import sys
from collections import deque
from pprint import pprint
import heapq
sys.stdin = open('1922.txt', 'rt')


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

heap = []
visited[1] = True
result = 0
cnt = 1
for a in graph[1]:
    heapq.heappush(heap, a)
while heap:
    cost, to = heapq.heappop(heap)
    if not visited[to]:
        visited[to] = True
        cnt += 1
        result += cost
        for u in graph[to]:
            heapq.heappush(heap, u)
    if cnt == V:
        break
print(result)
