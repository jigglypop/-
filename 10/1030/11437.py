import sys
from collections import deque
sys.stdin = open("11437.txt", "r")
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
depth = [0] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

Q = deque([1])
check = [False] * (N+1)
check[1] = True
while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not check[v]:
            check[v] = True
            depth[v] = depth[u] + 1
            parent[v] = u
            Q.append(v)


def LCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
