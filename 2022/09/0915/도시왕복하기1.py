from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/17412.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)

N, P = Split()
S = 1
E = 2
graph = A([], N + 1)
C = A(0, [N + 1, N + 1])
F = A(0, [N + 1, N + 1])
for _ in range(P):
    u, v = Split()
    graph[u].append(v)
    graph[v].append(u)
    C[u][v] = 1

def bfs(u):
    Q = deque([u])
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if C[u][v] > F[u][v] and parent[v] == -1:
                parent[v] = u
                Q.append(v)

count = 0
while True:
    parent = [-1] * (N + 1)
    parent[S] = S
    bfs(S)
    if parent[E] == -1:
        break
    v = E
    while v != S:
        F[parent[v]][v] += 1 
        F[v][parent[v]] -= 1
        v = parent[v]
    count += 1
print(count)
    