import sys
sys.stdin = open('11659.txt', 'r')
input, print = sys.stdin.readline, sys.stdout.write

N, M = map(int, input().split())
board = [0] + list(map(int, input().split()))

for i in range(N):
    board[i + 1] += board[i]

for _ in range(M):
    A, B = map(int, input().split())
    print(f"{board[B] - board[A - 1]}\n")
