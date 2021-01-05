import sys
from heapq import heappop, heappush
sys.stdin = open('10423.txt', 'r')
input = sys.stdin.readline


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


N, M, K = map(int, input().split())
A = list(map(int, input().split()))
edges = []
parent = list(range(N+1))
for i in range(1, K):
    union(A[i], A[i-1])
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()
result = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
print(result)
