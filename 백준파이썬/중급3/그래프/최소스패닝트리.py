import sys
sys.stdin = open("1197.txt", "r")
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
result = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)
