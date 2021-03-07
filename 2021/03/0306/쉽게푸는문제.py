import sys
sys.stdin = open("1292.txt", 'r')

A, B = map(int, input().split())
n = 0
DP = [0 for _ in range(B+1)]
for i in range(1, B + 1):
    for j in range(i):
        n += 1
        if n >= B+1:
            break
        DP[n] = DP[n-1] + i

print(DP[B] - DP[A - 1])
