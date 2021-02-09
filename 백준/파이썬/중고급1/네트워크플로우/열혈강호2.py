import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('11376.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
N = max(n, m)
graph = [[] for _ in range(N+1)]
pred = [-1 for _ in range(N+1)]


def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if pred[v] == -1 or dfs(pred[v]):
                pred[v] = u
                return True
        return False


for i in range(1, n+1):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]+1):
        graph[i].append(temp[j])

total = 0
for i in range(1, n + 1):
    for _ in range(2):
        check = [False for _ in range(N + 1)]
        if dfs(i):
            total += 1
print(total)
