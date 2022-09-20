from collections import deque
from copy import copy
import sys
sys.stdin = open('./text/1260.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)


N, M, V = Split()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = Split()
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i] = sorted(graph[i])

def dfs(u):
    visited[u] = True
    print(u, end=" ")
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

def bfs(u):
    visited[u] = True
    Q = deque([u])
    while Q:
        u = Q.popleft()
        print(u, end=" ")
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)

visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)