import sys
sys.stdin = open('5585.txt', 'r')

N = int(input())
M = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
count = 0
for coin in coins:
    print(coin)
    print(M//coin)
    print(M % coin)
    print('----------')
    count += M // coin
    M = M % coin
print(count)
