import sys
sys.stdin = open('./text/4196.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

for _ in range(Int()):
    N, M = Split()
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = Split()
        graph[a].append(b)

    visited = [False] * (N + 1)
    S = []
    count = 0

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            S.append(i)

    visited = [False] * (N + 1)
    while S:
        t = S.pop()
        if not visited[t]:
            dfs(t)
            count += 1

    print(count)