import sys
sys.stdin = open("./text/24479.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M, R = Split()
board = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = Split()
    board[u].append(v)
    board[v].append(u)

def dfs(v):
    global count
    visited[v] = count
    board[v].sort()
    for v in board[v]:
        if not visited[v]:
            count += 1
            dfs(v)

visited = [0] * (N + 1)
count = 1
dfs(R)

for i in range(1, N + 1):
    print(visited[i])