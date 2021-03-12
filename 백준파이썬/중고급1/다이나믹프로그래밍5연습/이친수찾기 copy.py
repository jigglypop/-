import sys
sys.stdin = open('2201.txt', 'r')
K = int(input())
DP = [0] * 101
S = [0] * 101
DP[1] = 1
for i in range(2, 101):
    DP[i] = DP[i-1] + DP[i-2]
for i in range(1, 101):
    S[i] = S[i-1] + DP[i]

if K == 1:
    print('1')
else:
    print('10', end='')
    n = 0
    for i in range(2, 101):
        if K <= S[i]:
            n = i
            break
    K -= S[n-1] + 1
    n -= 2
    while n > 0:
        if K > S[n-1]:
            if n >= 2:
                print('10', end='')
            else:
                print('1', end='')
            K -= S[n-1] + 1
            n -= 2
        else:
            print('0', end='')
            n -= 1
