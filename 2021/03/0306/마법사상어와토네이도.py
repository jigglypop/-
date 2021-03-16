import sys
sys.stdin = open("20057.txt", "r")
input = sys.stdin.readline
di = ((0, -1), (1, 0), (0, 1), (-1, 0))
N = int(input())
# 홀수
board = [[0] * N for _ in range(N)]
y = x = N // 2
d = 0
for i in range(1, N**2 + 1):
    board[y][x] = i
    y, x = y + di[d][0], x + di[d][1]
    if board[y + di[(d + 1) % 4][0]][x + di[(d + 1) % 4][1]] == 0:
        d = (d + 1) % 4

for b in board:
    print(*b)
