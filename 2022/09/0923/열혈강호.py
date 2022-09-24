from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/11375.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
N, M = Split()
MAX = max(N, M)
graph = [[] for _ in range(N + 1)]
parent = [-1] * (M + 1)
for i in range(1, N + 1):
    graph[i] = List()[1:]

def dfs(u):
    if not visited[u]:
        visited[u] = True
        for v in graph[u]:
            if parent[v] == -1 or dfs(parent[v]):
                parent[v] = u
                return True
    return False

result = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    if dfs(i):
        result += 1
print(result)

