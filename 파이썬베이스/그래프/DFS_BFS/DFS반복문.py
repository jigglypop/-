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


visited = [False] * 9
visited[1] = True
# print(u, end=" ")
S = [1]
while S:
    u = S.pop()
    print(u, end=" ")
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            S.append(v)
