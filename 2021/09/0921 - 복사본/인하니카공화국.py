from pprint import pprint
import sys
sys.stdin = open("./12784.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

def dfs(u):
    visited[u] = True 
    result = 0
    for v, c in tree[u]:
        if not visited[v]:
            result += min(c,  dfs(v))
    if result == 0:
        return INF
    else:
        return result

for _ in range(int(input())):
    N, M = map(int, input().split())
    tree=[[] for _ in range(N + 1)]
    visited = [False] *(N + 1)
    for _ in range(M):
        a, b, c = map(int,input().split())
        tree[a].append([b, c])
        tree[b].append([a, c])
    if N == 1:
        print(0)
    else:
        print(dfs(1))