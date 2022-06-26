from heapq import *
import sys
sys.stdin = open("./text/2150.txt", "r")
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for i in range(V + 1)]
_graph = [[] for i in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    _graph[b].append(a)
    
def dfs(u, Graph, S):
    visited[u] = True
    for v in Graph[u]:
        if not visited[v]:
            dfs(v, Graph, S)
    S.append(u)
S = []
visited = [False] * (V + 1)
for i in range(1, V+1):
    if not visited[i]:
        dfs(i, graph, S)
visited = [False] * (V+1)
results = []
while S:
    scc = []
    i = S.pop()
    if not visited[i]:
        dfs(i, _graph, scc)
        print(scc)
        results.append(sorted(scc) + [-1])