import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

n, m, K = Split()
N = max(n, m)
board = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]

def dfs(u):
    if visited[u]: return
    visited[u] = True
    for v in board[u]:
        if parent[v] == -1 or dfs(parent[v]):
            parent[v] = u
            return True
    return False

for i in range(1, n+1):
    temp = list(Split())
    for j in range(1, temp[0]+1):
        board[i].append(temp[j])

total = 0
count = 0
for i in range(1, n + 1):
    visited = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
for i in range(1, n + 1):
    while True:
        visited = [False for _ in range(N + 1)]
        if dfs(i):
            total += 1
            count += 1
        else: break
        if count == K: break
    if count == K: break
print(total)