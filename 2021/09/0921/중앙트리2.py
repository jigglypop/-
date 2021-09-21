from pprint import pprint
import sys
from collections import deque
sys.stdin = open('7812.txt', 'r')
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0: break
    tree = [[] for _ in range(N + 1)]
    visited = [False] * N
    board = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        board[a][b] = c
        board[b][a] = c
        tree[a].append(b)
        tree[b].append(a)

    value = [0] * N
    up  = [0] * N
    down = [1] * N
    def dfs(u, count):
        up[u] = count
        visited[u] = True
        for v in tree[u]:
            if not visited[v]:
                dfs(v, count + 1)
                down[u] += down[v]
                value[v] += board[u][v] * down[v]
    dfs(0, 0)
    down[0] = 0
    visited = [False] * N
    def dfs2(u):
        visited[u] = True
        for v in tree[u]:
            if not visited[v]:
                dfs2(v)
                value[u] += value[v]
    dfs2(0)
    print(value)
    print(down)
    print(tree)
    print('---')