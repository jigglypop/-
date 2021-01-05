import sys
sys.stdin = open('11657.txt', 'r')
inf = sys.maxsize

N, M = map(int, input().split())
graph = []
dist = [inf]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

cycle = False
dist[1] = 0
for i in range(N):
    for j in range(M):
        x, y, z = graph[j]
        if dist[x] != inf and dist[y] > dist[x] + z:
            dist[y] = dist[x] + z
            if i == N-1:
                cycle = True

if (cycle):
    print(-1)
else:
    if N == 1:
        print(dist[1])
    for i in range(2, len(dist)):
        print(dist[i] if dist[i] != inf else -1)
