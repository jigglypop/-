def DFS(v):
    visit[v] = True     
    print(v, end=" ")
    for w in G[v]:
        if not visit[w]:
            c += 1
            DFS(w)

# ----------------------------------------------
import sys
sys.stdin = open("DFSinput.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
c = 0
DFS(1)
