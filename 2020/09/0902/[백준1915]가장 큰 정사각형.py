import sys
from pprint import pprint
sys.stdin = open("1915.txt", "r")

Y, X = map(int, input().split())
board = [0] + [[0] + list(map(int, list(input()))) for _ in range(X)]
result = 0
memo = [[0]*(X+1) for _ in range(Y+1)]
for y in range(1, Y+1):
    for x in range(1, X+1):
        if board[y][x] == 0:
            continue
        memo[y][x] = min(memo[y-1][x-1], memo[y-1][x], memo[y][x-1]) + 1
        if result < memo[y][x]:
            result = memo[y][x]
print(result*result)
