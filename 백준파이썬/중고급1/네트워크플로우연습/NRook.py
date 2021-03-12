import sys
sys.stdin = open('1760.txt', 'r')
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
boardX = [[-1] * X for _ in range(Y)]
boardY = [[-1] * X for _ in range(Y)]


count = 1
flag = False
for y in range(Y):
    for x in range(X):
        if board[y][x] != 2:
            if board[y][x] == 1:
                continue
            if flag:
                flag = False
                count += 1
            boardX[y][x] = count
        else:
            flag = True
    flag = True

N = count
count = 1
flag = False
for x in range(X):
    for y in range(Y):
        if board[y][x] != 2:
            if board[y][x] == 1:
                continue
            if flag:
                flag = False
                count += 1
            boardY[y][x] = count
        else:
            flag = True
    flag = True
N += count

graph = [[] for _ in range(N+1)]
parent = [-1 for _ in range(N+1)]
for y in range(Y):
    for x in range(X):
        if board[y][x] == 0:
            graph[boardX[y][x]].append(boardY[y][x])


def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if parent[v] == -1 or dfs(parent[v]):
                parent[v] = u
                return True
        return False


total = 0
for i in range(N+1):
    check = [False for _ in range(N+1)]
    if dfs(i):
        total += 1
print(total)
