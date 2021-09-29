import sys
from pprint import pprint
sys.stdin = open("./text/16507.txt", "r")
input = sys.stdin.readline
Y, X, Q = map(int, input().split())
board = [[0] * (X + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(Y)] + [[0] * (X + 2)]
pprint(board)
for y in range(1, Y + 1):
    for x in range(1, X + 1):
        board[y][x] += board[y - 1][x] + board[y][x - 1] - board[y - 1][x - 1]
for _ in range(Q):
    sy, sx, ey, ex = map(int, input().split())
    sums = board[ey][ex] - board[ey][sx - 1] - board[sy - 1][ex] + board[sy - 1][sx - 1]
    counts = (ey - sy + 1) * (ex - sx + 1)
    print(sums // counts)