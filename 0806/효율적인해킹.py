import sys
sys.stdin = open('효율적인해킹.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def DFS(v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i, visited)


temp = [[0, i] for i in range(N+1)]
Max = 0
for i in range(N+1):
    visited = [False] * (N+1)
    DFS(i, visited)
    cnt = visited.count(True)
    temp[i][0] = cnt
    Max = max(cnt, Max)

for i in range(N+1):
    if temp[i][0] == Max:
        print(i, end=" ")
