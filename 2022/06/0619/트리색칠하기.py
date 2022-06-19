import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("./text/1693.txt", "r")
input = sys.stdin.readline

N = int(input())
INF = sys.maxsize
tree = [[] for _ in range(N + 1)]
dp = [[i for i in range(17)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

def dfs(u):
    visited[u] = True
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            for i in range(1, 17):
                dp[u][i] +=  min([INF] + dp[v][1:i] + dp[v][i + 1:])

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(min(dp[1][1:]))
