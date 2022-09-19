from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/2367.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)

n, k, d = Split()
S = 1
E = 2
N = n + d + 2
MAX = 2 * N + 1
limit = [0] + List()
graph = A([], MAX)
C = A(0, [MAX, MAX])
F = A(0, [MAX, MAX])
INF = sys.maxsize
# # 사람
for i in range(3, 3 + n):
    graph[i].append(i + N)
    graph[i + N].append(i)
    C[i + N][i] = k
# S -> 사람
    graph[i].append(S)
    graph[S].append(i)
    C[S][i] = 1
# 음식
for i in range(2 + n, 2 + n + d):
    graph[i].append(i + N)
    graph[i + N].append(i)
    C[i + N][i] = limit[i - n - 1]
# 음식 -> E
    graph[i + N].append(E)
    graph[E].append(i + N)
    C[i + N][E] = 1
# 그래프
for i in range(1, n + 1):
    temp = List()
    for cook in temp[1:]:
        u = i + 2
        v = cook + n + 2
        graph[u + N].append(v)
        graph[v].append(u + N)
        graph[v + N].append(u)
        graph[u].append(v + N)
        C[u][v + N] = INF
        C[v][u + N] = INF

def bfs(u):
    Q = deque([u])
    while Q:
        u = Q.popleft()
        for v in graph[u]:
            if parent[v] == -1 and C[u][v] > F[u][v]:
                parent[v] = u
                Q.append(v)

count = 0
while True:
    parent = [-1] * MAX
    parent[S] = S
    bfs(S)
    if parent[E] == -1:
        break
    v = E
    while v != S:
        F[parent[v]][v] += 1
        F[v][parent[v]] -= 1
        v = parent[v]
    count += 1
print(count)