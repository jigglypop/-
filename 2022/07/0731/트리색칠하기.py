import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/1298.txt', 'r')
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline
INF = sys.maxsize

N = Int()
tree = [[] for _ in range(N + 1)]
dp = [[i for i in range(17)] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

def dfs(u):
    visited[u] = True
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            for i in range(1, 17):
                temp = min([INF] + dp[v][1:i] + dp[v][i + 1:])
                dp[u][i] += temp

for _ in range(N - 1):
    a, b = Split()
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
print(min(dp[1][1:]))

