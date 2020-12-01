import sys
from pprint import pprint
sys.stdin = open('2240.txt', 'r')

input = sys.stdin.readline
S, W = map(int, input().split())
board = [0] + [int(input()) for _ in range(S)]
DP = [[[-1] * 2 for _ in range(W)] for _ in range(S+1)]
# 0 = 1, 1 = 2
