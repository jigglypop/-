import sys
from collections import deque
from pprint import pprint
import heapq
sys.stdin = open('1197.txt', 'rt')


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
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()
result = 0

for C, A, B in edges:
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        result += C
print(result)
