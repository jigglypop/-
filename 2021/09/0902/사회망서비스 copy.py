import sys
sys.setrecursionlimit(10**4)
sys.stdin = open("./2533.txt", "r")
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)

visited = [False for _ in range(N + 1)]


def dfs(u):
    dp[u][0] = 0
    dp[u][1] = 1
    for v in tree[u]:
        if not visited[v]:
            visited[v] = True
            print(v)
            dfs(v)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])


dfs(1)
print(dp)
