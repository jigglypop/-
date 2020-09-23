import sys
sys.stdin = open('11403.txt', 'r')


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for z in range(N):
    for y in range(N):
        for x in range(N):
            if graph[y][z] and graph[z][x]:
                graph[y][x] = 1
for i in graph:
    print(*i)
