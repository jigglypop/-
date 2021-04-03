import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('12995.txt', 'r')
input = sys.stdin.readline

mod = 1000000007


def dfs(u, parent):
    for v in tree[u]:
        if v != parent:
            child[u].append(v)
            dfs(v, u)


def go(i, e, K):
    if DP[i][e][K] != -1:
        return DP[i][e][K]
    if K == 0:
        return 1
    if e >= len(child[i]):
        return K == 1
    DP[i][e][K] = 0
    for j in range(K):
        DP[i][e][K] += go(child[i][e], 0, j) * go(i, e + 1, K - j)
    return DP[i][e][K]


N, K = map(int, input().split())
tree = [[] for _ in range(N+1)]
child = [[] * (N+1) for _ in range(N+1)]
DP = [[[-1] * (51) for _ in range(51)] for _ in range(51)]

for i in range(1, N):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, 0)
result = 0
for i in range(1, N+1):
    result += go(i, 0, K)
print(result % mod)
