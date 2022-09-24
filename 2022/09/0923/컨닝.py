from copy import copy, deepcopy
from pprint import pprint
import sys
sys.stdin = open('./text/11014.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def L(v, Args):
    if isinstance(Args, int):
        return [deepcopy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [deepcopy(v) for _ in range(Args[0])]
    return L([deepcopy(v) for _ in range(Args.pop())], Args)

for _ in range(Int()):
    Y, X = Split()
    MAX = Y * X + 1
    board = [list(Str()) for _ in range(Y)]
    di = ((-1, 0), (1, 0), (0, 1), (0, -1), (0, 0))
    graph = [[] for _ in range(MAX + 1)]
    for y in range(Y):
        for x in range(X):
            if board[y][x] == 'x':continue
            i = y * X + x
            for dy, dx in di:
                ny, nx = y + dy, x + dx
                if 0 <= ny < Y and 0 <= nx < X:
                    if board[ny][nx] != 'x':
                        j = ny * X + nx
                        graph[i].append(j)

    parent = [-1] * (MAX + 1)

    def dfs(u):
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                if parent[v] == -1 or dfs(v):
                    parent[v] = u
                    return True
        return False

    total = 0
    for i in range(1, MAX + 1):
        visited = [False] * (MAX + 1)
        if dfs(i):
            total += 1
    print(total)

