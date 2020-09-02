import sys
from collections import deque
sys.stdin = open("11438.txt", "r")


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depth = [0] * (N+1)
check = [False] * (N+1)
parent = [0] * (N+1)
check[1] = True
depth[1] = 0
Q = deque([1])

while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not check[v]:
            depth[v] = depth[u] + 1
            check[v] = True
            parent[v] = u
            Q.append(v)
