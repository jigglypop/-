import sys
sys.stdin = open("15685.txt", 'r')
input = sys.stdin.readline
N = int(input())
di = ((0, 1), (-1, 0), (0, -1), (1, 0))
plus = ((0, 0), (1, 0), (0, 1), (1, 1))
board = [[0] * 102 for _ in range(102)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    point = [[y, x]]
    n = 0
    while n <= g:
        if n == 0:
            ny, nx = y + di[d][0], x + di[d][1]
            point.append([ny, nx])
        else:
            pivot = point[-1]
            N = len(point) - 1
            for i in range(N-1, -1, -1):
                _y, _x = point[i][0] - pivot[0], point[i][1] - pivot[1]
                _y, _x = _x, -_y
                point.append([_y + pivot[0], _x + pivot[1]])
        n += 1
    for ny, nx in point:
        board[ny][nx] = 1
result = 0
for y in range(102):
    for x in range(102):
        flag = True
        for dy, dx in plus:
            ny, nx = y + dy, x + dx
            if board[ny][nx] != 1:
                flag = False
                break
        if flag:
            result += 1
print(result)
