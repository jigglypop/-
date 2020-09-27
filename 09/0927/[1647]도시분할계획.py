import sys
sys.stdin = open('1647.txt', 'r')

input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()
parent = [i for i in range(N+1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


Max = 0
result = 0
for C, A, B in edges:
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        Max = max(Max, C)
        result += C


print(result - Max)
