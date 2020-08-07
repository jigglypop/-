import sys
sys.setrecursionlimit(10**9)
sys.stdin = open("[백준11725]트리의부모찾기.txt", 'r')


N = int(input())
parent = [0 for _ in range(N+1)]
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def DFS(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(i, tree, parent)


DFS(1, tree, parent)
for i in range(2, N+1):
    print(parent[i])
