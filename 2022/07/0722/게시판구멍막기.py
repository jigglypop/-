from pprint import pprint
import sys
sys.stdin = open('./text/2414.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

Y, X = Split()
board = [list(Str()) for _ in range(Y)]
graph = [[] for _ in range(Y + 1)]
pred = [-1 for _ in range(Y + 1)]
for y in range(Y):
    for x in range(X):
        if board[y][x] == "*":
            graph[y + 1].append(x + 1)

def dfs(u):
    if not check[u]:
        check[u] = True
        for v in graph[u]:
            if pred[v] == -1 or dfs(pred[v]):
                pred[v] = u
                return True
        return False


total = 0
for i in range(1, Y + 1):
    check = [False for _ in range(Y + 1)]
    if dfs(i):
        total += 1

print(total)