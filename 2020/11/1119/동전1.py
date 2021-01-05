import sys
from pprint import pprint
sys.stdin = open('2293.txt', 'r')

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
DP = [0] * 10001
DP[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        DP[i] += DP[i-coin]
print(DP)
