import sys
sys.stdin = open("1197.txt", "r")


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


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
result = 0

for c, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(result)
