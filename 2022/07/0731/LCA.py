from math import log2
import sys
sys.stdin = open('./text/15480.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = Split()
    tree[a].append(b)
    tree[b].append(a)

depth = [0] * (N + 1)
prev = [[0] * 21 for _ in range(N + 1)]

def dfs(s):
    S = [s]
    depth[s] = 1
    while S:
        u = S.pop()
        for v in tree[u]:
            if depth[v]: 
                continue
            prev[v][0] = u
            depth[v] = depth[u] + 1
            S.append(v)
dfs(1)

for i in range(1, 21):
    for j in range(1,N + 1):
        prev[j][i] = prev[prev[j][i-1]][i-1]
        
def LCA(u, v):
    if depth[u] != depth[v]:
        if depth[u] > depth[v]:
            u, v = v, u
        for i in range(20, -1,-1):
            if depth[v] - depth[u] >= (1<<i):
                v = prev[v][i]
    if u == v: 
        return u
    for i in range(20,-1,-1):
        if prev[u][i] != prev[v][i]:
            u = prev[u][i]
            v = prev[v][i]
    return prev[u][0]

D = lambda x: [-depth[x], x]

for _ in range(Int()):
    a, b, c = Split()
    print(sorted([D(LCA(a, b)), D(LCA(b, c)), D(LCA(a, c))])[0][1])