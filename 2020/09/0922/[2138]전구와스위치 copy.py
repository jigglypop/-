import sys
import math
sys.stdin = open('2138.txt', 'r')

N = int(input())
before = list(input())
after = list(input())
_before = []
for i in range(2):
    _before.append(before)


def change(y, x, board):
    return '1' if board[y][x] == '0' else '0'


board = [['0' for _ in range(N)] for _ in range(4)]

for y in range(4):
    for x in range(N):
        if (y == 1 or y == 3) and x <= 1:
            board[y][x] = change(y, x, _before)
for y in range(4):
    for x in range(N):
        if y >= 2 and N-2 <= x <= N-1:
            board[y][x] = change(y, x, board)
Min = sys.maxsize
# for j in range(4):
#     count = math.ceil(j/2)
#     for i in range(1, N-1):
#         if board[j][i-1] != after[i-1]:
#             board[j][i-1] = change(j, i-1, board)
#             board[j][i] = change(j, i, board)
#             board[j][i+1] = change(j, i+1, board)
#             count += 1
#     if board[j] == after:
#         Min = min(Min, count)
# if Min == sys.maxsize:
#     print(-1)
# else:
#     print(Min)
