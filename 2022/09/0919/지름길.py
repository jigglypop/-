from copy import copy
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1446.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, D = Split()
graph = [[(i + 1, 1)] for i in range(D + 1)]
graph[-1] = []
for _ in range(N):
    a, b, c = Split()
    if b > D:continue
    graph[a].append((b, c))

INF = sys.maxsize
dist = [INF] * (D + 1)
Q = [(0, 0)]
dist[0] = 0
while Q:
    u, cost = heappop(Q)
    if dist[u] < cost:continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(Q, (v, dist[v]))

print(dist[D])