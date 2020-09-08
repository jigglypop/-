import sys
from pprint import pprint
sys.stdin = open("1654.txt", "r")


N, K = map(int, input().split())
board = [int(input()) for _ in range(N)]
pprint(board)
