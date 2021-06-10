import sys
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

SCC = []


def dfs(Graph, start):
    S = [start]
    temp = []
    while S:
        u = S.pop()
        visited[u] = True
        for v in Graph[u]:
            if not visited[v]:
                SCC.append(u)
                S.append(v)
        SCC.append(u)
        temp.append(u)
    return temp


for i in range(1, V+1):
    if not visited[i]:
        SCC.append(i)
        dfs(graph, i)

visited = [False] * (V+1)
results = []
for i in SCC:
    if not visited[i]:
        temp = dfs(_graph, i)
        temp.sort()
        results.append(temp + [-1])

results.sort()
print(len(results))
for r in results:
    print(*r)
