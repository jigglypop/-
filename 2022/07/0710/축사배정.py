import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def dfs(u):
    if visited[u]: return False
    visited[u] = True
    for v in board[u]:
        if not parent[v] or dfs(parent[v]):
            visited[u] = False
            parent[v] = u
            return True
    return False
n, m = Split()
board = {}

for i in range(1, n + 1):
    board[i] = list(Split())[1:]
visited = [False for _ in range(n + 1)]
parent = [False for _ in range(m + 1)]
result = 0
for i in range(1, n + 1):
    if dfs(i):
        result += 1
print(result)