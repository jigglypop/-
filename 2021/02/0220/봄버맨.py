import sys
from pprint import pprint
sys.stdin = open("16918.txt", 'r')
# Y, X, N = map(int, input().split())
# board = [list(input()) for _ in range(Y)]
# pprint(board)
# now = []

# # for _ in range(N):
# di = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# temp_set = set()
# now = []
# for y in range(Y):
#     for x in range(X):
#         if board[y][x] == 'O':
#             now.append((y, x))
# for y, x in now:
#     for dy, dx in di:
#         ny, nx = y + dy, x + dx
#         if board[ny][nx] == '.':

# print(now)
