import sys
sys.stdin = open('11048.txt', 'r')
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
DP = [[0] * X for _ in range(Y)]
DP[0][0] = board[0][0]
for i in range(1, X):
    DP[0][i] = board[0][i] + DP[0][i-1]
for i in range(1, Y):
    DP[i][0] = board[i][0] + DP[i-1][0]
for y in range(1, Y):
    for x in range(1, X):
        DP[y][x] = board[y][x] + max(DP[y-1][x-1], DP[y][x-1], DP[y-1][x])
print(DP[Y-1][X-1])
