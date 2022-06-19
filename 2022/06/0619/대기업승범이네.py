import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open("./text/17831.txt", "r")
input = sys.stdin.readline
N = int(input())
nums = [0, 0] + list(map(int, input().split()))
W = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for a in range(2, N + 1):
    b = nums[a]
    tree[b].append(a)

def dfs(u):
    for v in tree[u]:
        dfs(v)
        dp[u][0] += max(dp[v][0], dp[v][1])
    dp[u][1] = dp[u][0]
    for v in tree[u]:
        dp[u][1] = max(dp[u][1], dp[u][0] - max(dp[v][0], dp[v][1]) + (W[u] * W[v]) + dp[v][0])

dfs(1)
print(max(dp[1]))
# print(min(dp[1][1:]))
