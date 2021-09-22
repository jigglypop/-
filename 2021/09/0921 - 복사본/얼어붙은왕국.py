from pprint import pprint
import sys
sys.stdin = open("./9279.txt", "r")
input = sys.stdin.readline
INF = sys.maxsize

while True:
    try:
        N, C = map(int, input().split())
        tree = [[] for _ in range(N + 1)]
        for _ in range(N - 1):
            a, b, c = map(int, input().split())
            tree[a].append([b, c])
            tree[b].append([a, c])

        visited = [False] * (N + 1)
        visited[C] = True

        def dfs(u):
            visited[u] = True
            result = 0
            for v, c in tree[u]:
                if not visited[v]:
                    result += dfs(v) if len(tree[v]) > 1 else 0
                    return c
                else:
                    return 0
        
        print(dfs(C))
    except:
        break;