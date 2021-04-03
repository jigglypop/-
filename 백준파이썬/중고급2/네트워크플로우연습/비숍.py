import sys
from pprint import pprint
sys.stdin = open('2570.txt', 'r')
N = int(input())
M = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(M):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1
boardX = [[-1] * N for _ in range(N)]
boardY = [[-1] * N for _ in range(N)]

up = []
down = []
left = []
right = []
for y in range(N):
    left.append((y, 0))
    right.append((y, N-1))
for x in range(N):
    up.append((0, x))
    down.append((N-1, x))

head = left[::-1] + up[1:]
foot = up + right[1:]

count = 1
flag = False
for y, x in head:
    ny = y
    nx = x
    while 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] == 0:
            if flag:
                flag = False
                count += 1
            boardX[ny][nx] = count
        else:
            flag = True
        ny += 1
        nx += 1
    flag = True

n = count
count = 1
flag = False
for y, x in foot:
    ny = y
    nx = x
    while 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] == 0:
            if flag:
                flag = False
                count += 1
            boardY[ny][nx] = count
        else:
            flag = True
        ny += 1
        nx -= 1
    flag = True
n += count


graph = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
for y in range(N):
    for x in range(N):
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
for i in range(n+1):
    check = [False for _ in range(n+1)]
    if dfs(i):
        total += 1
print(total)
