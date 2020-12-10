import sys
sys.stdin = open('1967.txt', 'r')
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def dfs(start):
    S = [(start, 0)]
    check = [False] * (N+1)
    check[start] = True
    Max = 0
    root = 0
    while S:
        u, w = S.pop()
        if Max < w:
            Max = w
            root = u
        for v, dw in tree[u]:
            if not check[v]:
                check[v] = True
                S.append((v, w + dw))
    return Max, root


A, root = dfs(1)
Max, B = dfs(root)
print(Max)
