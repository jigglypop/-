import sys
from pprint import pprint
from heapq import heappop, heappush
INF = sys.maxsize

sys.stdin = open('14938.txt', 'r')
input = sys.stdin.readline
INF = sys.maxsize
n, m, r = map(int, input().split())
A = [0] + list(map(int, input().split()))
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
for y in range(1, n+1):
    for x in range(1, n+1):
        if y == x:
            graph[y][x] == 0

for z in range(1, n+1):
    for y in range(1, n+1):
        for x in range(1, n+1):
            if graph[y][x] > graph[y][z] + graph[z][x]:
                graph[y][x] = graph[y][z] + graph[z][x]
Max = 0
for y in range(1, n+1):
    sums = 0
    for x in range(1, n+1):
        if graph[y][x] <= m or y == x:
            sums += A[x]
    Max = max(Max, sums)
print(Max)
