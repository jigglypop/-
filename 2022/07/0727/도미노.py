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
        graph[b].append(a)

    id = 0
    visited = [0] * (N + 1)
    finished = [False] * (N + 1)
    S = []
    SCC = []

    def dfs(u):
        global id
        id += 1
        visited[u] = id
        prev = id
        S.append(u)
        for v in graph[u]:
            if not visited[v]:
                prev = min(prev, dfs(v))
            elif not finished[v]:
                prev = min(prev, visited[v])

        if prev == visited[u]:
            scc = []
            while True:
                top = S.pop()
                scc.append(top)
                finished[top] = True
                if top == u:
                    break
            SCC.append(sorted(scc))
        return prev
    for i in range(1, N + 1):
        if not visited[i]: 
            dfs(i)

    idx = 0
    ids = [-1] * (N + 1)
    visit = [0] * (N + 1)
    result = []
    while stack:
        ssc = []
        node = stack.pop()
        if visit[node] == 0:
            idx += 1
            reverse_dfs(node, visit, ssc)
            result.append(sorted(ssc))
    scc_indegree = [0] * (idx + 1)

    for i in range(1, N + 1):
        for ed in graph[i]:
            if ids[i] != ids[ed]:
                scc_indegree[ids[ed]] += 1
    cnt = 0
    for i in range(1, len(scc_indegree)):
        if scc_indegree[i] == 0:
            cnt += 1
    print(cnt)