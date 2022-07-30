import sys
sys.stdin = open('./text/1760.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

Y, X = Split()
board = [List() for _ in range(Y)]
_X = [[-1] * X for _ in range(Y)]
_Y = [[-1] * X for _ in range(Y)]
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
            _X[y][x] = count
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
            _Y[y][x] = count
        else:
            flag = True
    flag = True

N += count
graph = [[] for _ in range(N + 1)]
prev = [-1 for _ in range(N + 1)]
for y in range(Y):
    for x in range(X):
        if board[y][x] == 0:
            graph[_X[y][x]].append(_Y[y][x])

def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if prev[v] == -1 or dfs(prev[v]):
                prev[v] = u
                return True
        return False
total = 0
for i in range(N + 1):
    check = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
print(total)