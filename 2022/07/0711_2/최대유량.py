from collections import deque
from pprint import pprint
import sys
sys.stdin = open("./text/6086.txt")
input = sys.stdin.readline
def Split():return map(str, input().strip().split())
def Int():return int(input().strip())
def Ord(x): return ord(x) - 65 if x <= 'Z' else ord(x) - 71

N = 52
board = [[] for _ in range(N)]
F = [[0] * N for _ in range(N)]
C = [[0] * N for _ in range(N)]

for _ in range(Int()):
    a, b, c = Split()
    a, b, c = Ord(a), Ord(b), int(c)
    board[a].append(b)
    board[b].append(a)
    C[a][b] += c
    C[b][a] += c
S, E = Ord('A'), Ord('Z')

def bfs():
    visited = [-1] * N
    visited[S] = S
    Q = deque([S])
    while Q and visited[E] == -1:
        u = Q.popleft()
        for v in board[u]:
            if visited[v] == -1 and C[u][v] > F[u][v]:
                visited[v] = u
                Q.append(v)
    return visited

total = 0
while True:
    visited = bfs()
    if visited[E] == -1: break
    flow = sys.maxsize
    v = E
    while v != S:
        u = visited[v]
        flow = min(flow, C[u][v])
        v = u
    v = E
    while v != S:
        u = visited[v]
        C[v][u] += flow
        C[u][v] -= flow
        v = u
    total += flow
print(total)