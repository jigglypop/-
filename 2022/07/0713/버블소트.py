from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/1517.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N = Int()
board = list(Split())
_board = sorted(list(Split()))
# board = [0] * (2 * N)

# def update(i, x):
#     board[i] = x
#     while i > 1:
#         board[i // 2] = board[i] + board[i ^ 1]
#         i //= 2

# def query(l, r):
#     result = 0
#     while l <= r:
#         if l % 2 == 1:
#             result += board[l]
#             l += 1
#         if r % 2 == 0:
#             result += board[r]
#             r -= 1
#         l >>= 1
#         r >>= 1
#     return result
    
# result = 0
# for i in _factory:
#     update(i, 1)
#     result += query(i + 1, 2 * N - 1)
# print(result)
