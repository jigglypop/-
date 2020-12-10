import sys
sys.stdin = open('1167.txt', 'r')
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    temp = list(map(int, input().split()))
    x = temp[0]
    temp = temp[1:]
    temp.pop()
    for i in range(0, len(temp), 2):
        tree[x].append((temp[i], temp[i+1]))


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


_, root = dfs(1)
Max, _ = dfs(root)
print(Max)
