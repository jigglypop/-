import sys
from pprint import pprint
sys.stdin = open('2458.txt', 'r')

# 입력
N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
for k in range(1, N+1):
    for y in range(1, N+1):
        for x in range(1, N+1):
            if graph[y][x] == 1 or (graph[y][k] == 1 and graph[k][x] == 1):
                graph[y][x] = 1
answer = 0
for y in range(1, N+1):
    known_graph = 0
    for x in range(1, N+1):
        known_graph += graph[y][x] + graph[x][y]
    if known_graph == N-1:
        answer += 1
print(answer)
