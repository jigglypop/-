import sys
sys.stdin = open('1717.txt', 'r')


N, M = map(int, input().split())
parent = [i for i in range(N+1)]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(paernt, b, c):
    b = find(parent, b)
    c = find(parent, c)
    if b > c:
        parent[b] = c
    else:
        parent[c] = b


v, e = map(int, input().split())
parent = [i for i in range(v+1)]
rank = [0 for _ in range(v+1)]


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] = rank[b] + 1


for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union(parent, b, c)
    else:
        if find(parent, b) == find(parent, c):
            print('YES')
        else:
            print('NO')
