import sys
from pprint import pprint
sys.stdin = open('1867.txt')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if parent[v] == -1 or dfs(parent[v]):
                parent[v] = u
                return True
        return False


total = 0
for i in range(1, N+1):
    check = [False for _ in range(N+1)]
    if dfs(i):
        total += 1

print(total)
