import sys
from math import *
sys.stdin = open('./text/11053.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

N = Int()
board = list(Split())
dp = [1] * N
for i in range(N):
    for j in range(i):
        if board[i] > board [j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))