import sys
sys.stdin = open('집합의표현.txt', 'r')
input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [i for i in range(v+1)]

for i in range(e):
    p, a, b = map(int, input().split())
    if p == 0:
        union(parent, a, b)
    else:
        if find(parent, a) == find(parent, b):
            print('YES')
        else:
            print('NO')
