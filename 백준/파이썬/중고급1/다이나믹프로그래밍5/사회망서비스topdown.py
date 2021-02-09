import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('2533.txt', 'r')
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
DP = [[-1, -1] for _ in range(N+1)]
check = [False for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def go(u, include):
    result = DP[u][include]
    if result != -1:
        return result
    check[u] = True
    result = include
    for v in tree[u]:
        if check[v]:
            continue
        if include == 0:
            result += go(v, 1)
        else:
            result += min(go(v, 0), go(v, 1))
    check[u] = False
    DP[u][include] = result
    return result


print(min(go(1, 0), go(1, 1)))
