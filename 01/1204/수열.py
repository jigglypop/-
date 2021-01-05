import sys
from pprint import pprint
sys.stdin = open('2559.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
board = list(map(int, input().split()))
print(board)
Sum = sum(board[0:K])
left = right = 0
print(Sum)
Max = Sum
i = 0
for i in range(i, N-K):
    Sum -= board[i]
    Sum += board[K]
    K += 1
    Max = max(Max, Sum)
print(Max)
