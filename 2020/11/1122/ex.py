import sys
sys.stdin = open('2294.txt', 'r')
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
DP = [10001] * (K+1)
DP[0] = 0
for coin in coins:
    for i in range(coin, K+1):
        DP[i] = min(DP[i], DP[i-coin] + 1)
print(-1) if DP[K] == 10001 else print(DP[K])
