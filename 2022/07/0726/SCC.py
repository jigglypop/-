import sys
sys.stdin = open('./text/2150.txt', 'r')
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M = Split()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = Split()
    graph[a].append(b)

id = 0
visited = [0] * (N + 1)
finished = [0] * (N + 1)
s = []
SCC = []

def dfs(u):
    global id
    id += 1
    visited[u] = id
    prev = id
    s.append(u)
    for v in graph[u]:
        if not visited[v]:
            prev = min(prev, dfs(v))
        elif not finished[v]:
            prev = min(prev, visited[v])
    
    if prev == visited[u]:
        scc = []
        while True:
            t = s.pop()
            scc.append(t)
            finished[t]=1
            if t == u: 
                break
        SCC.append(sorted(scc))
    return prev

for i in range(1, N + 1):
    if not visited[i]: 
        dfs(i)
SCC.sort()
print(len(SCC))
for scc in SCC:
    print(*(scc + [-1]))