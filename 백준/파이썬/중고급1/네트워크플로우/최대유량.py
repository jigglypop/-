import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open('6086.txt')
input = sys.stdin.readline


def convert(x):
    return ord(x) - 65 if x == x.upper() else ord(x) - 71


C = [[0] * 52 for _ in range(52)]
path = [[] for _ in range(52)]
for _ in range(int(input())):
    a, b, c = map(str, input().split())
    a, b, c = convert(a), convert(b), int(c)
    C[a][b] += c
    C[b][a] += c
    path[a] += [b]
    path[b] += [a]

prev = [-1] * 52
S = convert('A')
E = convert('Z')
total = 0


def DFS(S, E):
    Q = [S]
    visited = [False] * 52
    visited[S] = True
    while Q:
        u = Q.pop()
        for v in path[u]:
            if C[u][v] > 0 and not visited[v]:
                visited[v] = True
                Q.append(v)
                prev[v] = u
    return visited[E]


while DFS(S, E):
    flow = sys.maxsize
    x = E
    while x != S:
        flow = min(flow, C[prev[x]][x])
        x = prev[x]
    x = E
    while x != S:
        C[x][prev[x]] += flow
        C[prev[x]][x] -= flow
        x = prev[x]
    total += flow
print(total)
