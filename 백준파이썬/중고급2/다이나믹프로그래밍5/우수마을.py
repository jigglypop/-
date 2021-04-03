import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('1949.txt', 'r')
input = sys.stdin.readline

N = int(input())
W = [0] + list(map(int, input().split()))
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
DP = [[0, 0] for i in range(N+1)]


def dfs(u, parent):
    DP[u][0] = 0
    DP[u][1] = W[u]
    for v in tree[u]:
        if v != parent:
            dfs(v, u)
            DP[u][0] += max(DP[v][0], DP[v][1])
            DP[u][1] += DP[v][0]


dfs(1, 0)
print(max(DP[1][0], DP[1][1]))
