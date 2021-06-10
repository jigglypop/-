import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('4196.txt', "r")
input = sys.stdin.readline
for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    _graph = [[] for _ in range(V+1)]
    SCC = [0] * (V+1)
    indegree = [0] * (V+1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        _graph[b].append(a)

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        S.append(u)

    def dfs2(u, i):
        SCC[u] = i
        for v in _graph[u]:
            if SCC[v] == 0:
                dfs2(v, i)
            elif SCC[v] != SCC[u]:
                indegree[SCC[u]] += 1

    visited = [False] * (V + 1)
    S = []
    for i in range(1, V+1):
        if not visited[i]:
            dfs(i)

    i = 0
    while S:
        now = S.pop()
        if SCC[now] == 0:
            SCC[now] = i
            dfs2(now, i)
            i += 1
    result = 0
    for j in range(1, i):
        if indegree[j] == 0:
            result += 1
    print(result)
