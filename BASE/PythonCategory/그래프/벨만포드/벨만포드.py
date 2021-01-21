from heapq import heappop, heappush
import sys
sys.stdin = open("11657.txt", "r")
# https://www.acmicpc.net/problem/11657
input = sys.stdin.readline
INF = sys.maxsize
Y, X = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(X)]


def BellmanFord():
    dist = [INF]*(Y+1)
    dist[1] = 0
    for y in range(Y):
        for x in range(X):
            u, v, cost = edges[x]
            if dist[u] != INF and dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if y == Y-1:
                    return [-1]
    if Y == 1:
        return [dist[1]]
    return list(map(lambda x: x if x != INF else -1, dist[2:]))


results = BellmanFord()
for result in results:
    print(result)
