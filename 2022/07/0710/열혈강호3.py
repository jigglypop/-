import sys
sys.stdin = open('./text/11377.txt', 'r')
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M, K = Split()
N = max(N, M)
board = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]

def dfs(u):
    if visited[u]:return False
    visited[u] = True
    for v in board[u]:
        if parent[v] == -1 or dfs(parent[v]):
            parent[v] = u
            return True
    return False

for i in range(1, N + 1):
    board[i] += list(Split())[1:]

total = 0
count = 0
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
        count += 1
    if count == K: break
print(total)

