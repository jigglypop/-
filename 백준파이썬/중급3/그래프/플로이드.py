import sys
sys.stdin = open("11404.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for y in range(n):
    for x in range(n):
        if y == x:
            graph[y][x] = 0
for z in range(n):
    for y in range(n):
        for x in range(n):
            if graph[y][x] > graph[y][z] + graph[z][x]:
                graph[y][x] = graph[y][z] + graph[z][x]
for y in range(n):
    for x in range(n):
        if graph[y][x] == INF:
            graph[y][x] = 0
for g in graph:
    print(*g)
