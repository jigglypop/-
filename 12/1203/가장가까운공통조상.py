from pprint import pprint
import sys
from math import log2
from collections import deque
sys.stdin = open('3584.txt', 'r')
input = sys.stdin.readline


def LCA(u, v, depth, P):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(logN-1, -1, -1):
        if depth[u] - depth[v] >= (1 << i):
            u = P[u][i]

    if u == v:
        return v

    for i in range(logN-1, -1, -1):
        if P[u][i] != P[v][i]:
            u = P[u][i]
            v = P[v][i]
    return P[u][0]


T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    logN = int(log2(N)) + 1
    parent = [0] * (N+1)
    depth = [0] * (N+1)
    check = [False] * (N+1)
    root = [False] * (N+1)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        if not root[b]:
            root[b] = True
        tree[b].append(a)
    start = 0
    for i in range(1, N+1):
        if not root[i]:
            start = i
    a, b = map(int, input().split())
    Q = deque([start])
    check[start] = True
    depth[start] = 0
    while Q:
        u = Q.popleft()
        for v in tree[u]:
            if not check[v]:
                Q.append(v)
                parent[v] = u
                depth[v] = depth[u] + 1
                check[v] = True

    P = [[0] * logN for _ in range(N+1)]
    for i in range(1, N+1):
        P[i][0] = parent[i]
    for j in range(1, logN):
        for i in range(1, N+1):
            P[i][j] = P[P[i][j-1]][j-1]

    print(LCA(a, b, depth, P))
