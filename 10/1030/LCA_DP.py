import sys
from collections import deque
from math import log2
sys.stdin = open("dp.txt", "r")
input = sys.stdin.readline

N = int(input())
logN = int(log2(N)+1)
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0 for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
check = [True for _ in range(N+1)]
Q = deque([1])
while Q:
    u = Q.popleft()
    check[u] = False
    for v in tree[u]:
        if check[v]:
            Q.append(v)
            parent[v] = u
            depth[v] = depth[u] + 1

DP = [[0 for _ in range(logN)] for i in range(N+1)]
for i in range(N+1):
    DP[i][0] = parent[i]
for j in range(1, logN):
    for i in range(1, N+1):
        DP[i][j] = DP[DP[i][j-1]][j-1]


M = int(input())


def LCA(a, b):
    if depth[b] > depth[a]:
        a, b = b, a

    for i in range(logN):
        if depth[a]-depth[b] & (1 << i):
            a = DP[a][i]

    if a == b:
        return a

    for i in range(logN-1, -1, -1):
        if DP[a][i] != DP[b][i]:
            a = DP[a][i]
            b = DP[b][i]
    return DP[b][0]


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(LCA(a, b))
