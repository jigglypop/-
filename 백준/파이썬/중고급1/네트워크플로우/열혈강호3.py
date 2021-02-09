import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('11377.txt', 'r')
input = sys.stdin.readline
# 각 직원은 기본적으로 1개의 일을 할 수 있지만, K명은 2개까지 할 수 있습니다.
n, m, K = map(int, input().split())
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
count = 0
for i in range(1, n + 1):
    check = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
for i in range(1, n + 1):
    check = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
        count += 1
    if count == K:
        break
print(total)
