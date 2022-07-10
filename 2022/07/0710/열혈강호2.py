import sys
sys.stdin = open('./text/11376.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

n, m = Split()
N = max(n, m)
board = [[] for _ in range(N + 1)]
parent = [ -1 for _ in range(N + 1)]

def dfs(u):
    if visited[u]:return False
    visited[u] = True
    for v in board[u]:
        if parent[v] == -1 or dfs(parent[v]):
            parent[v] = u
            return True
    return False

for i in range(n):
    temp = list(Split())
    board[i + 1] += temp[1:]

total = 0
for i in range(1, n + 1):
    for _ in range(2):
        visited = [False for _ in range(N + 1)]
        if dfs(i):
            total += 1
print(total)