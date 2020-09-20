import sys
from collections import deque
sys.stdin = open('16948.txt', 'r')


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*N for _ in range(N)]


def BFS():
    di = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
    Q = deque([(r1, c1)])
    while Q:
        r, c = Q.popleft()
        if r == r2 and c == c2:
            print(visited[r][c])
            return
        for dr, dc in di:
            nr, nc = r + dr, c+dc
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    Q.append((nr, nc))
    print(-1)
    return


BFS()
