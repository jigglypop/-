from pprint import pprint
import sys
sys.stdin = open("./text/1956.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

V, E = Split()
INF = sys.maxsize
board = [[INF] * V for _ in range(V)]
for _ in range(E):
    a, b, c = Split()
    board[a - 1][b - 1] = min(board[a - 1][b - 1], c)

for z in range(V):
    for y in range(V):
        for x in range(V):
            board[y][x] = min(board[y][x], board[y][z] + board[z][x])

res = INF
for i in range(V):
    res = min(res, board[i][i])

if res == INF:
    print(-1)
else:
    print(res)