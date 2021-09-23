from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/7812.txt', 'r')
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
    dp = [0] * N
    down = [0] * N
    up = [0] * N

    def dfs(u):
        visited[u] = True
        for v in tree[u]:
            if not visited[v]:
                dp[v] += dp[u] + board[u][v]
                dfs(v)
                up[v] += up[u] + 1
                down[u] += down[v] + 1
    dfs(0)
    visited = [False] * N

    def track(u, x):
        if u == x:
            return
        visited[u] = True
        for v in tree[u]:
            if not visited[v]:
                track(v, x)

    track(0, 5)
    All = sum(dp)
    sums = dp[::]
    print(tree)
    for i in range(1, N):
        sums[i] += sums[i - 1]
    print(dp)
    print(sums)
    print('------')