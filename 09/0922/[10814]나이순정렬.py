import sys
sys.stdin = open('10814.txt', 'r')

N = int(input())
board = [list(map(str, input().split())) for _ in range(N)]

board.sort(key=lambda x: int(x[0]))
for b in board:
    print(*b)
