import sys
from collections import deque
sys.stdin = open('2567.txt', 'r')
input = sys.stdin.readline


def bfs(i, j):
    q = deque()
    visited[i][j] = True
    q.append([i, j])
    rtn = 0
    while q:
        i, j = q.popleft()
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni <= 101 and 0 <= nj <= 101:
                if not visited[ni][nj]:
                    if board[ni][nj]:
                        visited[ni][nj] = True
                        q.append([ni, nj])
                    else:
                        rtn += 1
    return rtn


def putPaper(i, j):
    for ni in range(i, i+10):
        for nj in range(j, j+10):
            board[ni][nj] = 1


N = int(input())
board = [[0]*102 for _ in range(102)]
visited = [[False]*102 for _ in range(102)]
ans = 0
for _ in range(N):
    i, j = map(int, input().split())
    putPaper(i, j)

for i in range(102):
    for j in range(102):
        if board[i][j] and not visited[i][j]:
            ans += bfs(i, j)
print(ans)
