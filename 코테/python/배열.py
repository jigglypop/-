import math
import os
import random
import re
import sys
from pprint import pprint
from collections import deque


arr = 'ABC'
result = []

# 배열조작

# board = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# y = 1
# x = 1
# #  -1,-1   -1, 0    -1,1
# #   0,-1    0, 0     0,1
# #   1,-1    1, 0     1,1
# di = [(-1, -1), (-1, 0), (-1, 1),
#       (0, -1), (0, 0), (0, 1),
#       (1, -1), (1, 0), (1, 1)]
# # 북서 -1, -1
# ny, nx = y + di[0][0], x + di[0][1]
# print(board[ny][nx])
# # 위 -1, 0
# ny, nx = y + di[1][0], x + di[1][1]
# print(board[ny][nx])
# # 북동 -1, 1
# ny, nx = y + di[2][0], x + di[2][1]
# print(board[ny][nx])
# # 서 0, -1
# ny, nx = y + di[3][0], x + di[3][1]
# print(board[ny][nx])
# # 가운데 0, 0
# ny, nx = y + di[4][0], x + di[4][1]
# print(board[ny][nx])
# # 동 0, 1
# ny, nx = y + di[5][0], x + di[5][1]
# print(board[ny][nx])
# # 남서 1, -1
# ny, nx = y + di[6][0], x + di[6][1]
# print(board[ny][nx])
# # 아래 1, 0
# ny, nx = y + di[7][0], x + di[7][1]
# print(board[ny][nx])
# # 남동 1, 1
# ny, nx = y + di[8][0], x + di[8][1]
# print(board[ny][nx])


# 90도 돌리기

# def rotate90(y, board):
#     Y = len(board)
#     X = len(board[0])
#     return [[board[~y][x] for y in range(Y)] for x in range(X)]

# 180도 돌리기

# def rotate180(y, board):
#     Y = len(board)
#     X = len(board[0])
#     return [[board[~y][~x] for x in range(X)] for y in range(Y)]

# 270도 돌리기

# def rotate270(y, board):
#     Y = len(board)
#     X = len(board[0])
#     return [[board[y][~x] for y in range(Y)] for x in range(X)]


# 45도

# import sys
# sys.stdin = open("17276.txt", "r")
# input = sys.stdin.readline
# for _ in range(int(input())):
#     N, d = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     if d < 0:
#         d += 360
#     N_ = N // 2
#     di = [[] for _ in range(4)]
#     values = [[] for _ in range(4)]
#     for i in range(N):
#         di[0].append((i, i))
#         values[0].append(board[i][i])
#     for i in range(N):
#         di[1].append((i, N_))
#         values[1].append(board[i][N_])
#     for i in range(N-1, -1, -1):
#         di[2].append((~i, i))
#         values[2].append(board[~i][i])
#     for i in range(N-1, -1, -1):
#         di[3].append((N_, i))
#         values[3].append(board[N_][i])
#     di += list(map(lambda di: di[::-1], di))
#     values += list(map(lambda di: di[::-1], values))
#     turn = d // 45
#     _values = values[8 - turn:] + values[:8 - turn]
#     for j in range(8):
#         for i in range(N):
#             ny, nx = di[j][i]
#             val = _values[j][i]
#             board[ny][nx] = val
#     list(map(lambda a: print(*a), board))


# y기준 자르기

# def sliceY(y, board):
#     Y = len(board)
#     X = len(board[0])
#     return [board[y][x] for x in range(X)]

# x기준 자르기

# def sliceX(x, board):
#     Y = len(board)
#     X = len(board[0])
#     return [board[y][x] for y in range(Y)]

def oddNumbers(l, r):
    # Write your code here
    Q = deque()
    Q.append(1)
    print(Q)
    return [i for i in range(l, r+1) if i % 2 == 1]


print(oddNumbers(1, 8))
