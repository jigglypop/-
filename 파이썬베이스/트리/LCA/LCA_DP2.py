import sys
from collections import deque
from math import log2
sys.stdin = open("11438.txt", "r")
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
depth = [0] * (N + 1)
parent = [0] * (N + 1)
Q = deque([1])
depth[1] = 1
while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not depth[v]:
            Q.append(v)
            depth[v] = depth[u] + 1
            parent[v] = u
log2N = int(log2(N)) + 1
DP = [[0] * log2N for _ in range(N + 1)]
for i in range(N+1):
    DP[i][0] = parent[i]
for j in range(1, log2N):
    for i in range(1, N+1):
        DP[i][j] = DP[DP[i][j-1]][j-1]

for _ in range(int(input())):
    u, v = map(int, input().split())
    if depth[u] < depth[v]:
        u, v = v, u
    for i in range(log2N - 1, -1, -1):
        if depth[u] - depth[v] >= (1 << i):
            u = DP[u][i]
    if u == v:
        print(u)
        continue
    for i in range(log2N - 1, -1, -1):
        if DP[u][i] != DP[v][i]:
            u = DP[u][i]
            v = DP[v][i]
    print(DP[u][0])
