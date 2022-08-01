import sys
from collections import deque
sys.stdin = open('./text/2316.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()


def dfs(u):
    if u == 2: return 1
    for v in range(2, 2 * N + 1):
        if graph[u][v] and not visited[v]:            
            visited[v] = 1
            if dfs(v):
                graph[u][v] -= 1
                graph[v][u] += 1
                return 1
    return 0

N, M = Split()
graph = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
for i in range(1, N + 1):
    graph[i][i + N] = 1
for _ in range(M):
    a, b = Split()
    graph[a + N][b] += 1
    graph[b + N][a] += 1

result = 0
flow = 1
while flow:
    visited = [0] * (2 * N + 1)
    flow = dfs(1 + N)
    result += flow
print(result)