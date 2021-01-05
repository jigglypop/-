import sys
sys.stdin = open('9095.txt', 'r')

input = sys.stdin.readline
limit = 10000
DP = [0] * (limit + 1)
DP[0] = 1
for j in range(1, 4):
    for i in range(1, limit+1):
        if i - j >= 0:
            DP[i] += DP[i-j]
for _ in range(int(input())):
    n = int(input())
    print(DP[n])
