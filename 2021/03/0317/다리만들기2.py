import sys
from pprint import pprint
from itertools import combinations
sys.stdin = open("17472.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(Y)]
islands = []


def dfs(sy, sx, count):
    visited = [[False] * X for _ in range(Y)]
    temp = set()
    S = [(sy, sx)]
    visited[sy][sx] = True
    maps[sy][sx] = count
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while S:
        y, x = S.pop()
        for dy, dx in di:
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if maps[ny][nx] == 0:
                    temp.add((y, x, count))
                elif maps[ny][nx] == 1 and not visited[ny][nx]:
                    maps[ny][nx] = count
                    visited[ny][nx] = True
                    S.append([ny, nx])
    return list(temp)


count = 2
for y in range(Y):
    for x in range(X):
        if maps[y][x] == 1:
            islands += dfs(y, x, count)
            count += 1


def road(y, x, count):
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    temp = []
    for dy, dx in di:
        ny, nx = y, x
        while True:
            ny += dy
            nx += dx
            if 0 > ny or Y <= ny or 0 > nx or X <= nx:
                break
            elif maps[ny][nx] == count:
                break
            elif maps[ny][nx] != count and maps[ny][nx] != 0:
                if abs(ny-y) + abs(nx-x) - 1 > 1:
                    temp.append((abs(ny-y) + abs(nx-x) - 1,
                                 min(count - 2, maps[ny][nx] - 2),
                                 max(count - 2, maps[ny][nx] - 2)))
                break
    return temp


V = len(islands)
edges = []
for island in islands:
    edges += road(*island)
edges = list(set(edges))
parent = [i for i in range(V + 1)]


def find(x):
    return x if parent[x] == x else find(parent[x])


def union(a, b):
    parent[find(b)] = find(a)


edges.sort()
result = 0
n = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        n += 1
        result += c
print(result if n == count-3 else -1)
