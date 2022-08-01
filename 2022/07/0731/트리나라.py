import sys
sys.setrecursionlimit(10 ** 5)
sys.stdin = open('./text/12995.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

P = 1000000007
def dfs(u, prev):
    for v in tree[u]:
        if v != prev:
            child[u].append(v)
            dfs(v, u)

def go(i, e, K):
    if dp[i][e][K] != -1:
        return dp[i][e][K]
    if K == 0:
        return 1
    if e >= len(child[i]):
        return K == 1
    dp[i][e][K] = 0
    for j in range(K):
        dp[i][e][K] += go(child[i][e], 0, j) * go(i, e + 1, K - j)
    return dp[i][e][K]

N, K = Split()
tree = [[] for _ in range(N + 1)]
child = [[] * (N + 1) for _ in range(N + 1)]
dp = [[[-1] * (51) for _ in range(51)] for _ in range(51)]
for i in range(1, N):
    a, b = Split()
    tree[a].append(b)
    tree[b].append(a)

dfs(1, 0)
result = 0
for i in range(1, N + 1):
    result += go(i, 0, K)
print(result % P)

