import sys
sys.stdin = open('10159.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
for y in range(N+1):
    for x in range(N+1):
        if y == x:
            graph[y][x] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
for z in range(1, N+1):
    for y in range(1, N+1):
        for x in range(1, N+1):
            if graph[y][z] == 1 and graph[z][x] == 1:
                graph[y][x] = 1
for y in range(1, N+1):
    count = 0
    for x in range(1, N+1):
        if graph[y][x] == INF and graph[x][y] == INF:
            count += 1
    print(count)
