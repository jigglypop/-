from collections import deque
from copy import copy
from pprint import pprint
import sys
from math import *
sys.stdin = open('./text/3584.txt', 'r')
input = sys.stdin.readline
d = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [copy(n) for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

def LCA(u, v, D, P):
    if D[u] < D[v]:
        u, v = v, u
    for i in range(logN - 1, -1, -1):
        if D[u] - D[v] >= (1 << i):
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
    board = L([], [N + 1])
    logN = int(log2(N)) + 1
    parent = [0] * (N + 1)
    D = [0] * (N + 1)
    visited = [False] * (N + 1)
    root = [False] * (N + 1)

    for _ in range(N-1):
        a, b = Split()
        board[a].append(b)
        if not root[b]:
            root[b] = True
        board[b].append(a)

    S = 0
    for i in range(1, N + 1):
        if not root[i]:
            S = i
    a, b = Split()
    Q = deque([S])
    visited[S] = True
    D[S] = 0

    while Q:
        u = Q.popleft()
        for v in board[u]:
            if not visited[v]:
                Q.append(v)
                parent[v] = u
                D[v] = D[u] + 1
                visited[v] = True

    P = L(0, [N + 1, logN])
    for i in range(1, N + 1):
        P[i][0] = parent[i]
    for j in range(1, logN):
        for i in range(1, N + 1):
            P[i][j] = P[P[i][j-1]][j-1]
    print(LCA(a, b, D, P))