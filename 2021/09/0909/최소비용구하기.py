from heapq import heappop, heappush
import sys
sys.stdin = open('1916.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())
Q = [(0, s)]
dist = [INF] * (N + 1)
dist[s] = 0
while Q:
    w, u = heappop(Q)
    if dist[u] < w:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(Q, (dist[v], v))
print(dist[e])