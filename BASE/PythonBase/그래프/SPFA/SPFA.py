import sys
from collections import deque
sys.stdin = open("11657.txt", "r")

input = sys.stdin.readline
INF = sys.maxsize
Y, X = map(int, input().split())
graph = [[] for _ in range(Y+1)]
for _ in range(X):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def SPFA():
    dist = [INF] * (Y+1)
    check = [False] * (Y+1)
    count = [0] * (Y+1)

    dist[1] = 0
    Q = deque([1])
    check[1] = True
    while Q:
        u = Q.popleft()
        check[u] = False
        for cost, v in graph[u]:
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
                if not check[v]:
                    Q.append(v)
                    check[v] = True
                    count[v] += 1
                    if count[v] >= Y:
                        return [-1]
    if Y == 1:
        return [dist[1]]
    return list(map(lambda x: x if x != INF else -1, dist[2:]))


results = SPFA()
for result in results:
    print(result)
