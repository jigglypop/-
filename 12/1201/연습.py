import sys
sys.stdin = open('2169.txt', 'r')

input = sys.stdin.readline
Y, X = map(int, input().split())
board = [0] + [[0] + list(map(int, input().split())) for _ in range(Y)]
DP = [[[-sys.maxsize] * 3 for _ in range(X + 2)] for _ in range(Y+1)]
DP[1][1][1] = board[1][1]
for x in range(2, X+1):
    DP[1][x][1] = DP[1][x-1][1] + board[1][x]
for y in range(2, Y+1):
    for x in range(1, X+1):
        DP[y][x][0] = max(DP[y-1][x][0], DP[y-1][x][1],
                          DP[y-1][x][2]) + board[y][x]
        DP[y][x][1] = max(DP[y][x-1][0], DP[y][x-1][1]) + board[y][x]
    for x in range(X, 0, -1):
        DP[y][x][2] = max(DP[y][x+1][0], DP[y][x+1][2]) + board[y][x]
print(max(DP[Y][X]))
