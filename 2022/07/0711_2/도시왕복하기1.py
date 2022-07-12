from collections import deque
import sys
sys.stdin = open("./text/17412.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N, M = Split()
board = [[] for _ in range(N + 1)]
C = [[0] * (N + 1) for _ in range(N + 1)]
F = [[0] * (N + 1) for _ in range(N + 1)]
s, e = 0, 1
for _ in range(M):
    u, v = Split()
    u -= 1
    v -= 1
    board[u].append(v)
    board[v].append(u)
    C[u][v] = 1
total = 0

def bfs():
    visited = [-1] * (N + 1)
    visited[s] = s
    Q = deque([s])
    while Q and visited[e] == -1:
        u = Q.popleft()
        for v in board[u]:
            if C[u][v] > F[u][v] and visited[v] == -1:
                visited[v] = u
                Q.append(v)
    return visited

while True:
    visited = bfs()
    if visited[e] == -1:
        print(total)
        break
    v = e
    while v != s:
        u = visited[v]
        F[u][v] += 1
        F[v][u] -= 1
        v = u
    total += 1
