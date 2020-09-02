import sys
sys.setrecursionlimit(2000*2000)

sys.stdin = open("1937.txt", "r")
di = ((0, 1), (0, -1), (1, 0), (-1, 0))
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
memo = [[0]*N for _ in range(N)]


def go(y, x):
    if memo[y][x] != 0:
        return memo[y][x]
    memo[y][x] = 1
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N:
            if board[y][x] < board[ny][nx]:
                memo[y][x] = max(memo[y][x], go(ny, nx) + 1)
    return memo[y][x]


result = 0
for y in range(N):
    for x in range(N):
        result = max(result, go(y, x))
print(result)
