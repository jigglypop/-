import sys
input = sys.stdin.readline
def Split():return map(int, input().strip().split())

N, M = Split()
board = [[] for _ in range(N+1)]
pred = [-1 for _ in range(N+1)]
for _ in range(M):
    a, b = Split()
    board[a].append(b)

def dfs(u):
    if not visited[u]:
        visited[u] = True
        for v in board[u]:
            if pred[v] == -1 or dfs(pred[v]):
                pred[v] = u
                return True
        return False
        
total = 0
for i in range(1, N+1):
    visited = [False for _ in range(N+1)]
    if dfs(i):
        total += 1
print(total)