import heapq
import sys

sys.stdin = open("6497.txt", "r")

input = sys.stdin.readline


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    edges = []
    # heapq.heapify(q)
    total = 0
    ans = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        edges.append((c, b, a))
        total += c
    edges.sort()
    for edge in edges:
        dist, s, e = edge
        if find(parent, s) != find(parent, e):
            union(parent, s, e)
            ans += dist
    print(total - ans)
