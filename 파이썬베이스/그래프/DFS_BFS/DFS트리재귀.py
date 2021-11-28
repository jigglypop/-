graph = [
    [],
    [2, 3],     # 1
    [1, 4, 5],  # 2
    [1, 6, 7],  # 3
    [2],        # 4
    [2],        # 5
    [3],        # 6
    [3],        # 7
]


def DFS(u, visited):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            DFS(v, visited)
            print(v, end=" ")


visited = [False] * 9
DFS(1, visited)
