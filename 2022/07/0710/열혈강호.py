from pprint import pprint
import sys
sys.stdin = open('./text/11375.txt', 'r')
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
def Split():return map(int, input().strip().split())

a, b = Split()
N = max(a, b)
board = [[] for _ in range(N + 1)]
parent = [-1 for _ in range(N + 1)]
for i in range(a):
    temp = list(Split())[1:]
    board[i + 1] += temp

def dfs(u):
    if visited[u]: return
    visited[u] = True
    for v in board[u]:
        if parent[v] == -1 or dfs(parent[v]):
            parent[v] = u
            return True
    return False

total = 0
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]
    if dfs(i):
        total += 1
print(total)