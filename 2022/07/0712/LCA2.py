from collections import deque
from copy import copy
from pprint import pprint
import sys
from math import *
sys.stdin = open('./text/11438.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [copy(n) for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N = Int()
board = L([], [N + 1])
logN = int(log2(N)) + 1
D = [0] * (N + 1)
parent = [0] * (N + 1)
dp = L(0, [N + 1, logN])
for _ in range(N - 1):
    a, b = Split()
    board[a].append(b)
    board[b].append(a)


def bfs():
    visited = [False] * (N + 1)
    Q = deque([1])
    visited[1] = True
    while Q:
        u = Q.popleft()
        for v in board[u]:
            if not visited[v]:
                visited[v] = True
                D[v] = D[u] + 1
                parent[v] = u
                Q.append(v)

bfs()
for i in range(N + 1):
   dp[i][0] = parent[i]

for j in range(1, logN):
    for i in range(1, N + 1):
       dp[i][j] = dp[dp[i][j-1]][j-1]


def LCA(u, v):
    if D[u] < D[v]:
        u, v = v, u
    for i in range(logN - 1, -1, -1):
        if D[u] - D[v] >= (1 << i):
            u = dp[u][i]
    if u == v:
        return v
    for i in range(logN - 1, -1, -1):
        if dp[u][i] != dp[v][i]:
            u = dp[u][i]
            v = dp[v][i]
    return dp[u][0]

for _ in range(Int()):
    a, b = Split()
    print(LCA(a, b))