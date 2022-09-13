from collections import deque
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1967.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, cost = Split()
    tree[u].append([v, cost])
    tree[v].append([u, cost])

def bfs(u):
    visited = [-1] * (N + 1)
    visited[u] = 0
    PQ = []
    Q = deque([u])
    while Q:
        u = Q.popleft()
        for v, cost in tree[u]:
            if visited[v] == -1:
                Q.append(v)
                visited[v] = visited[u] + cost
                heappush(PQ, (-visited[v], v))
    return heappop(PQ)

A, u = bfs(1)
B, _ = bfs(u)
print(-B)