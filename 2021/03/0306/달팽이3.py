import sys
from pprint import pprint
sys.stdin = open("1959.txt", "r")
Y, X = map(int, input().split())
Q = [[0, 0]]
di = ((0, 1), (1, 0), (0, -1), (-1, 0))
board = [[0] * X for _ in range(Y)]
d = 0
count = 1
turn = 0
while Q:
    if count >= Y * X:
        y, x = Q.pop()
        print(turn)
        print(y+1, x+1)
        break
    y, x = Q.pop()
    board[y][x] = count
    if 0 <= y + di[d][0] < Y and 0 <= x + di[d][1] < X:
        if board[y + di[d][0]][x + di[d][1]] == 0:
            Q.append((y + di[d][0], x + di[d][1]))
        else:
            d = (d + 1) % 4
            turn += 1
            Q.append((y + di[d][0], x + di[d][1]))
    else:
        d = (d + 1) % 4
        turn += 1
        Q.append((y + di[d][0], x + di[d][1]))
    count += 1
