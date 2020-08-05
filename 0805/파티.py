import sys
from heapq import heappop, heappush
sys.stdin = open("파티.txt", "r")
INF = sys.maxsize
input = sys.stdin.readline


def Dijkstra(x):
    distance = [INF]*n
    heappush(heap, [0, x])
    d[x] = 0
    while heap:
        w, x = heappop(heap)
        for nw, nx in a[x]:
            nw += w
            if nw < distance[nx]:
                distance[nx] = nw
                heappush(heap, [nw, nx])
    return distance


n, m, t = map(int, input().split())
graph = [[]*n for _ in range(n)]
heap = []

for i in range(m):
    x, y, w = map(int, input().split())
    graph[x-1].append([w, y-1])

ans = [0]*n
for i in range(n):
    d = Dijkstra(i)
    ans[i] += d[t-1]
    d = Dijkstra(t-1)
    ans[i] += d[i]
print(max(ans))
