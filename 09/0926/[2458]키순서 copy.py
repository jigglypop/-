import sys
from pprint import pprint
from functools import lru_cache

sys.stdin = open('2458.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1


@lru_cache(maxsize=256)
def solve():
    for z in range(N):
        for y in range(N):
            for x in range(N):
                if graph[y][z] + graph[z][x] == 2:
                    graph[y][x] = 1


solve()
result = [0] * N
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            result[y] += 1
            result[x] += 1
print(result.count(N-1))
