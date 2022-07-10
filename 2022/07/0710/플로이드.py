from pprint import pprint
import sys
sys.stdin = open("./text/11404.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N = Int()
INF = sys.maxsize
board = [[INF] * N for _ in range(N)]
for _ in range(Int()):
    a, b, c = Split()
    board[a - 1][b - 1] = min(board[a - 1][b - 1], c)
for i in range(N):
    board[i][i] = 0

for z in range(N):
    for y in range(N):
        for x in range(N):
            board[y][x] = min(board[y][x], board[y][z] + board[z][x])

for y in range(N):
    for x in range(N):
        if board[y][x] == INF:
            board[y][x] = 0
for b in board:
    print(*b)