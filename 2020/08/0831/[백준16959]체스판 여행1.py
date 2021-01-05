import sys
from collections import deque
from pprint import pprint
sys.stdin = open("16959.txt", 'r')

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dist = [[[[-1] * 3 for _ in range(N*N)] for _ in range(N)] for _ in range(N)]

di_knight = ((-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2), (-2, -1))
di_rook = ((0, 1), (0, -1), (1, 0), (-1, 0))
di_bishop = ((1, 1), (1, -1), (-1, 1), (-1, -1))

Q = deque()
for y in range(N):
    for x in range(N):
        graph[y][x] -= 1
        if graph[y][x] == 0:
            for z in range(3):
                dist[y][x][0][z] = 0
                Q.append((y, x, 0, z))
ans = -1
while Q:
    y, x, num, piece = Q.popleft()
    if num == N * N - 1:
        if ans == -1 or ans > dist[y][x][num][piece]:
            ans = dist[y][x][num][piece]
    for p in range(3):
        if piece == p:
            continue
        if dist[y][x][num][p] == -1:
            dist[y][x][num][p] = dist[y][x][num][piece] + 1
            Q.append((y, x, num, p))
        # knight
        if piece == 0:
            for dy, dx in di_knight:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    next_num = num
                    if graph[ny][nx] == num + 1:
                        next_num = num + 1
                    if dist[ny][nx][next_num][piece] == -1:
                        dist[ny][nx][next_num][piece] = dist[y][x][num][piece] + 1
                        Q.append((ny, nx, next_num, piece))
        # rook
        elif piece == 1:
            for dy, dx in di_rook:
                l = 1
                while True:
                    ny = y + dy * l
                    nx = x + dx * l
                    if 0 <= ny < N and 0 <= nx < N:
                        next_num = num
                        if graph[ny][nx] == num + 1:
                            next_num = num + 1
                        if dist[ny][nx][next_num][piece] == -1:
                            dist[ny][nx][next_num][piece] = dist[y][x][num][piece] + 1
                            Q.append((ny, nx, next_num, piece))
                    else:
                        break
                    l += 1
        # bishop
        else:
            for dy, dx in di_bishop:
                l = 1
                while True:
                    ny = y + dy * l
                    nx = x + dx * l
                    if 0 <= ny < N and 0 <= nx < N:
                        next_num = num
                        if graph[ny][nx] == num + 1:
                            next_num = num + 1
                        if dist[ny][nx][next_num][piece] == -1:
                            dist[ny][nx][next_num][piece] = dist[y][x][num][piece] + 1
                            Q.append((ny, nx, next_num, piece))
                    else:
                        break
                    l += 1

print(ans)
