import sys
sys.stdin = open('2751.txt', 'r')


N = int(input())
board = [int(input()) for _ in range(N)]
board.sort()
for b in board:
    print(b)
