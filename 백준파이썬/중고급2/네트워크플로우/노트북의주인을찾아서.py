import sys
sys.stdin = open('1298.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
pred = [-1 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if pred[v] == -1 or dfs(pred[v]):
                pred[v] = u
                return True
        return False


total = 0
for i in range(1, N+1):
    check = [False for _ in range(N+1)]
    if dfs(i):
        total += 1
print(total)
