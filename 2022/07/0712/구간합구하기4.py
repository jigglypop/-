from heapq import heappop, heappush
import sys
from math import *
sys.stdin = open('./text/11659.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N, M = Split()
board = list(Split())
for i in range(1, N):
    board[i] += board[i - 1]
board = [0] + board
for _ in range(M):
    a, b = Split()
    print(board[b] - board[a - 1])