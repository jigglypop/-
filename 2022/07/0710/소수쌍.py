from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1017.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N = Int()
board = list(Split())
M = max(board) * 2
check = [False, False] + [True] * 2000
primes = []
for i in range(2, 2001):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, 2001, i):
            check[j] = False

_A = [0]
_B = [0]
for b in board:
    if b % 2: _A.append(b)
    else: _B.append(b)
if board[0] == _A[1]:
    A = _A[::]
    B = _B[::]
else:
    A = _B[::]
    B = _A[::]

board = [[] for _ in range(len(A))]
for a in range(1, len(A)):
    for b in range(1, len(B)):
        if check[A[a] + B[b]]:
            board[a].append(b)

def dfs(u):
    if visited[u] == 1: return False
    visited[u] = True
    for v in board[u]:
        if parent[v] == -1 or dfs(parent[v]):
            parent[v] = u
            return True
    return False

result = []
for i in board[1]:
    parent = [-1 for _ in range(len(B))]
    parent[i] = 1
    total = 1
    for j in range(1, len(A)):
        visited = [False for _ in range(len(A))]
        visited[1] = True
        total += dfs(j)
    if total == N // 2:
        result.append(B[i])

result.sort()
if not result:
    print(-1)
else:
    for r in result:
        print(r, end=" ")