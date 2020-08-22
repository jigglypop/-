import sys
sys.stdin = open('123더하기.txt', 'r')


def plus(n):
    if n == 1:
        memo[1] = 1
        return 1
    if n == 2:
        memo[2] = 2
        return 2
    if n == 3:
        memo[3] = 4
        return 4
    memo[n] = plus(n-3) + plus(n-2) + plus(n-1)
    return memo[n]


T = int(input())
for _ in range(T):
    N = int(input())
    memo = [0] * (N+1)
    print(plus(N))
