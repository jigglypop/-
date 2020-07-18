import sys
sys.stdin = open('피보나치.txt', 'r')


def fibonacci(n):
    global one, zero
    if n == 1:
        one += 1
        memo[1] = 1
        return memo[1]
    elif n == 0:
        zero += 1
        memo[0] = 0
        return memo[0]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    memo = [0] * (N+1)

    one = 0
    zero = 0
    fibonacci(N)
    print(memo)
    print('{} {}'.format(zero, one))
