import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("./1949.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [False for _ in range(N + 1)]


def dfs(u):
    dp[u][0] = 0
    dp[u][1] = nums[u]
    for v in tree[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v)
            dp[u][0] += max(dp[v])
            dp[u][1] += dp[v][0]


visited[1] = True
dfs(1)
print(max(dp[1]))
