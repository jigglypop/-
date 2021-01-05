import sys
sys.stdin = open('10870.txt', 'r')

N = int(input())


if N == 0:
    print(0)
else:
    DP = [0] * N
    for i in range(N):
        if i < 1:
            DP[i] = 1
        else:
            DP[i] = DP[i-2] + DP[i-1]
    print(DP[-1])
