import sys
sys.stdin = open("[백준9372]상근이의여행.txt", "r")


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


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
        a, b = map(int, input().split())
        graph.append((a, b))
    parent = [i for i in range(N+1)]
    cost = 0
    for a, b in graph:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            cost += 1
    print(cost)
