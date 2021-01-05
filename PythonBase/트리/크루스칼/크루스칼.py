import sys
sys.stdin = open("1922.txt", 'r')

# 크루스칼 순서
V = int(input())
E = int(input())
parent = [i for i in range(V+1)]

edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()
result = 0


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[min(a, b)] = max(a, b)


for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)
