import sys
from tkinter.tix import Tree
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("./text/2533.txt", "r")
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = 1
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v])
dfs(1)
print(min(dp[1]))