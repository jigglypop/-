import sys
sys.setrecursionlimit(100000)
sys.stdin = open('2213.txt', 'r')
input = sys.stdin.readline

N = int(input())
W = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
DP = [[0, 0] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def go(u, parent):
    for i in range(len(tree[u])):
        v = tree[u][i]
        if parent == tree[u][i]:
            continue
        go(tree[u][i], u)
    DP[u][1] = W[u]
    DP[u][0] = 0
    for i in range(len(tree[u])):
        v = tree[u][i]
        if parent == v:
            continue
        DP[u][1] += DP[v][0]
        DP[u][0] += max(DP[v][0], DP[v][1])


go(1, 0)
print(max(DP[1][0], DP[1][1]))

result = []


def gogo(x, y, parent):
    if y == 0:
        for i in range(len(tree[x])):
            v = tree[x][i]
            if parent == v:
                continue
            if DP[v][0] < DP[v][1]:
                gogo(v, 1, x)
            else:
                gogo(v, 0, x)
    elif y == 1:
        result.append(x)
        for i in range(len(tree[x])):
            v = tree[x][i]
            if parent == v:
                continue
            gogo(v, 0, x)


if DP[1][0] < DP[1][1]:
    gogo(1, 1, 0)
else:
    gogo(1, 0, 0)
sorted(result)
print(*result)
