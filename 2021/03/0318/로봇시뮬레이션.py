import sys
sys.stdin = open("2174.txt", "r")
input = sys.stdin.readline
X, Y = map(int, input().split())
N, M = map(int, input().split())
direct = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
di = ((-1, 0), (0, 1), (1, 0), (0, -1))
board = [[0] * X for _ in range(Y)]
points = [[]]

for i in range(N):
    x, y, c = list(input().split())
    x = int(x) - 1
    y = abs(Y - (int(y) - 1) - 1)
    c = int(direct[c])
    points.append((y, x, c))
    board[y][x] = i + 1

result = 'OK'
for _ in range(M):
    t, order, c = list(input().split())
    t = int(t)
    c = int(c)
    y, x, d = points[t]
    board[y][x] = 0
    if order == 'L':
        nd = (d - c) % 4
        points[t] = y, x, nd
    elif order == 'R':
        nd = (d + c) % 4
        points[t] = y, x, nd
    else:
        ny, nx = y + di[d][0] * c, x + di[d][1] * c
        temp = ''
        for i in range(1, c+1):
            ty, tx = y + di[d][0] * i, x + di[d][1] * i
            if 0 > ty or Y <= ty or 0 > tx or X <= tx:
                temp = f"Robot {str(t)} crashes into the wall"
                break
            if board[ty][tx] != 0:
                temp = f"Robot {str(t)} crashes into robot {board[ty][tx]}"
                break
        if temp != '':
            result = temp
            break
        else:
            points[t] = ny, nx, d
            board[ny][nx] = t
print(result)
