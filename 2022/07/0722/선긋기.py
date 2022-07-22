from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/2170.txt', 'r')
input = sys.stdin.readline
def List():return list(map(int, input().split()))
def Int():return int(input())

N = Int()
board = [List() for _ in range(N)]
board.sort()
l, r = board[0]
result = 0
for i in range(1, N):
    if board[i][1] <= r: continue
    elif board[i][0] <= r < board[i][1]:
        r = board[i][1]
    elif r < board[i][0]:
        result += r - l
        l = board[i][0]
        r = board[i][1]
result += r - l
print(result)