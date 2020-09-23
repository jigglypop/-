import sys
sys.stdin = open('11404.txt', 'r')

N = int(input())
M = int(input())
graph = [[sys.maxsize] * N for _ in range(N)]
for _ in range(M):
    a, b, c, = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

for i in range(N):
    graph[i][i] = 0

for z in range(N):
    for y in range(N):
        for x in range(N):
            if graph[y][x] > graph[y][z] + graph[z][x]:
                graph[y][x] = graph[y][z] + graph[z][x]

for y in range(N):
    for x in range(N):
        if graph[y][x] == sys.maxsize:
            graph[y][x] = 0
for g in graph:
    print(*g)
