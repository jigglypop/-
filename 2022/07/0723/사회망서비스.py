import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/2533.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = 1
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v])

N = Int()
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = Split()
    tree[a].append(b)
    tree[b].append(a)

visited = [False for _ in range(N + 1)]
dfs(1)
print(min(dp[1]))