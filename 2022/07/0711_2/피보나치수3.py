import sys
sys.stdin = open("./text/2749.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N = Int()
P = 1000000
Pi = 1500000
dp = [0] * (Pi + 1)
dp[1] = dp[2] = 1
for i in range(3, Pi + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % P
print(dp[N % Pi])
