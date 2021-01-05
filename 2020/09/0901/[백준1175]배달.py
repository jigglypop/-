from collections import deque
import sys
sys.stdin = open("1175.txt", 'r')

Y, X = map(int, input().split())
board = [list(input()) for _ in range(Y)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
end = [(0, 0)]
Q = deque()

dist = [[[[0] * 3 for _ in range(len(di))]
         for _ in range(X)] for _ in range(Y)]

for y in range(Y):
    for x in range(X):
        if board[y][x] == 'S':
            for i in range(4):
                Q.append((y, x, i, 0))
                dist[y][x][i][0] = 1
        if board[y][x] == 'C':
            end.append((y, x))
result = -1
while Q:
    y, x, direction, endpoint = Q.popleft()
    for i in range(4):
        if i != direction:
            ny = y + di[i][0]
            nx = x + di[i][1]
            if 0 <= ny < Y and 0 <= nx < X and dist[ny][nx][i][endpoint] == 0 and board[ny][nx] != '#':
                if ny == end[1][0] and nx == end[1][1]:
                    if endpoint == 2:
                        result = dist[y][x][direction][endpoint] if result == - \
                            1 else min(dist[y][x][direction][endpoint], result)
                    else:
                        dist[ny][nx][i][1] = dist[y][x][direction][endpoint] + 1
                        Q.append((ny, nx, i, 1))
                elif ny == end[2][0] and nx == end[2][1]:
                    if endpoint == 1:
                        result = dist[y][x][direction][endpoint] if result == - \
                            1 else min(dist[y][x][direction][endpoint], result)
                    else:
                        dist[ny][nx][i][2] = dist[y][x][direction][endpoint] + 1
                        Q.append((ny, nx, i, 2))
                else:
                    dist[ny][nx][i][endpoint] = dist[y][x][direction][endpoint] + 1
                    Q.append((ny, nx, i, endpoint))
print(result)
