import sys
sys.stdin = open("16926.txt", 'r')
input = sys.stdin.readline
Y, X, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
for i in range(min(Y, X) // 2):
    x, y, temp, d = i, i, [], 0
    temp.append((x, y, board[x][y]))
    while True:
        x, y = x + dx[d], y + dy[d]
        if x == -1 + i or x == Y - i or y == -1 + i or y == X - i:
            x, y = x - dx[d], y - dy[d]
            d += 1
            x, y = x + dx[d], y + dy[d]
        if x == i and y == i:
            break
        temp.append((x, y, board[x][y]))
    for j in range(len(temp)):
        nx, ny, v = temp[j]
        board[nx][ny] = temp[(j - K) % len(temp)][2]
for x in board:
    print(*x)
