from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/1017.txt', 'r')
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
A = [0]
B = [0]
check = [True for i in range(2000)]
result = []
check[1] = False
for i in range(2, 50):
    if check[i] == True:
        for j in range(i * 2, 2000, i):
            check[j] = False

def dfs(u):
    if visit[u] == 1:return 0
    visit[u] = 1
    for v in board[u]:
        if parent[v] == 0 or dfs(parent[v]):
            parent[v] = u
            return 1
    return 0

for i in range(n):
    if s[0] % 2 == s[i] % 2:A.append(s[i])
    else:B.append(s[i])
print(A)
print(B)

board = [[] for _ in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if check[A[i] + B[j]]:
            board[i].append(j)
print(board)
for i in board[1]:
    parent = [0 for _ in range(len(B))]
    parent[i] = 1
    total = 1
    for j in range(1, len(A)):
        visit = [0 for _ in range(len(A))]
        visit[1] = 1
        total += dfs(j)
    if total == n // 2:
        result.append(B[i])
    print(parent)
if not result:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r, end=" ")