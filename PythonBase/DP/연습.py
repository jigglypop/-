def fibonacci(n):
    DP[0] = 0
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]


n = int(input())
DP = [-1] * (n+1)
fibonacci(n)
print(DP[n])
