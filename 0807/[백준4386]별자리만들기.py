from sys import stdin
import sys
sys.stdin = open("[백준4386]별자리만들기.txt", "r")


def get_dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def get_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]


def union_parent(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if x < y:
        parent[y] = x
        tree_sz[x] += tree_sz[y]
    else:
        parent[x] = y
        tree_sz[y] += tree_sz[x]


n = int(stdin.readline())
location = []
for _ in range(n):
    location.append(list(map(float, stdin.readline().split())))
dist = []
for i in range(len(location)):
    for j in range(i + 1, len(location)):
        dist.append([get_dist(location[i], location[j]), i, j])

parent = [i for i in range(len(location))]
tree_sz = [1 for i in range(len(location))]

dist.sort()

ans = 0
for i in range(len(dist)):
    if get_parent(dist[i][1]) != get_parent(dist[i][2]):
        ans += dist[i][0]
        union_parent(dist[i][1], dist[i][2])
        if tree_sz[get_parent(dist[i][1])] == len(location):
            break

print(round(ans, 3))
