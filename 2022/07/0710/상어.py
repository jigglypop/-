import sys
input = sys.stdin.readline
N = int(input())
def Split():return map(int, input().strip().split())
sharks = [list(Split()) for _ in range(N)]
board = [[] for _ in range(N)]
for i in range(len(sharks)):
    for j in range(len(sharks)):
        if i == j:continue
        if sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] and sharks[i][2] >= sharks[j][2]:
            if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1] and sharks[i][2] == sharks[j][2]:
                if i > j:
                    board[i].append(j)
                else:
                    board[j].append(i)
            else:
                board[i].append(j)
def dfs(u):
    if not visited[u]:
        visited[u] = True
        for v in board[u]:
            if parent[v] == -1 or dfs(parent[v]):
                parent[v] = u
                return True
        return False

parent = [-1 for _ in range(N)]
total = 0
for i in range(N):
    for _ in range(2):
        visited = [False for _ in range(N)]
        if dfs(i):
            total += 1
print(len(parent) - total)