import sys
from collections import deque
from itertools import combinations
sys.stdin = open("17142.txt", "r")

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    cnt, cnt2 = 0, 0
    while q:
        qlen = len(q)
        flag, flag2 = 0, 1
        for idx in range(qlen):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == 0:
                    if a[nx][ny] == 0 or a[nx][ny] == 2:
                        c[nx][ny] = 1
                        q.append([nx, ny])
                        flag = 1
                        if a[nx][ny] == 0:
                            flag2 = 0

        if flag == 1:
            if flag2 == 0:
                if cnt2:
                    cnt += cnt2 + 1
                    cnt2 = 0
                else:
                    cnt += 1
            else:
                cnt2 += 1

    for i in range(n):
        for j in range(n):
            if (a[i][j] == 0 or a[i][j] == 2) and c[i][j] == 0:
                return sys.maxsize
    return cnt


n, m = map(int, input().split())
a, v = [], []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    for j in range(n):
        if a[i][j] == 2:
            v.append([i, j])
k = list(combinations(v, m))
ans = sys.maxsize
for i in range(len(k)):
    q = deque()
    c = [[0] * n for _ in range(n)]
    for j in range(m):
        x, y = k[i][j][0], k[i][j][1]
        c[x][y] = 1
        q.append([x, y])

    ans = min(ans, bfs())

print(-1) if ans == sys.maxsize else print(ans)
