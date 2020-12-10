import sys
from collections import deque
sys.stdin = open('11725.txt', 'r')
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (N+1)
check = [False] * (N+1)
check[1] = True
Q = deque([1])
while Q:
    u = Q.popleft()
    for v in tree[u]:
        if not check[v]:
            parent[v] = u
            check[v] = True
            Q.append(v)

for i in range(2, N+1):
    print(parent[i])
