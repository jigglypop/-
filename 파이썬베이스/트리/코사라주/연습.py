import sys
sys.setrecursionlimit(10**4)
sys.stdin = open("2150.txt", "r")
input = sys.stdin.readline
V, E = map(int, input().split())
visited = [False] * (V + 1)
graph = [[] for i in range(V + 1)]
_graph = [[] for i in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    _graph[b].append(a)


def dfs(u, visited, S):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            S.append(v)
            dfs(v, visited, S)
    S.append(u)


def _dfs(u, visited, S):
    visited[u] = True
    for v in _graph[u]:
        if not visited[v]:
            _dfs(v, visited, S)
    S.append(u)


S = []
for i in range(1, V+1):
    if not visited[i]:
        dfs(i, visited, S)

visited = [0] * (V+1)
results = []

while S:
    scc = []
    node = S.pop()
    if not visited[node]:
        _dfs(node, visited, scc)
        results.append(sorted(scc) + [-1])
results.sort()
print(len(results))
for r in results:
    print(*r)
