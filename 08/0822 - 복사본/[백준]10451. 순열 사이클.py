import sys
sys.stdin = open("10451.txt", "r")


T = int(input())
for _ in range(T):
    N = int(input())
    board = list(map(int, input().split()))
    print(board)
