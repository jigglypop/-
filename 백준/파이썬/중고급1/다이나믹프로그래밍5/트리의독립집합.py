import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('2213.txt', 'r')
input = sys.stdin.readline

N = int(input())
W = [0] + list(map(int, input().split()))
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
DP = [[0, 0] for i in range(N+1)]


def go(u, parent):
    DP[u][1] = W[u]
    for v in tree[u]:
        if v != parent:
            go(v, u)
            DP[u][0] += max(DP[v][0], DP[v][1])
            DP[u][1] += DP[v][0]


result = []


def track(u, parent, last):
    if not last:
        if DP[u][0] < DP[u][1]:
            result.append(u)
            last = True
    else:
        last = False
    for v in tree[u]:
        if v != parent:
            track(v, u, last)


go(1, 0)
track(1, 0, False)
print(max(DP[1]))
print(*sorted(result))
