from pprint import pprint
import sys
sys.stdin = open('./text/2579.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
board = [0] + [Int() for _ in range(N)]
if N == 1:
    print(board[1])
else:
    dp = [0] * (N + 1)
    dp[1] = board[1]
    dp[2] = board[1] + board[2] 
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + board[i - 1] + board[i], dp[i - 2] + board[i])  
    print(dp[N])