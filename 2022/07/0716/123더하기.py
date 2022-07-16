
import sys
sys.stdin = open('./text/9095.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()
board = [Int() for _ in range(Int())]
print(board)
N = max(board)
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for b in board:
    print(dp[b])