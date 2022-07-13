from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/2606.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [copy(n) for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N = Int()
M = Int()
board = L([], [N + 1])
for _ in range(M):
    a, b = Split()
    board[a].append(b)
    board[b].append(a)
visited = [False] * (N + 1)
Q = deque([1])
visited[1] = True
while Q:
    u = Q.popleft()
    for v in board[u]:
        if not visited[v]:
            visited[v] = True
            Q.append(v)
result = 0
for v in visited:
    if v:
        result += 1
print(result - 1)