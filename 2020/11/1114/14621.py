import sys
sys.stdin = open('14621.txt', 'r')

N, M = map(int, input().split())
A = ['*'] + list(map(str, input().split()))
parent = list(range(N+1))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if A[b] != A[a]:
        edges.append((c, a, b))
edges.sort()
result = 0
count = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
        count += 1

print(result) if count == N-1 else print(-1)
