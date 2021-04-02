import sys
sys.stdin = open("12101.txt", "r")
input = sys.stdin.readline
DP = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]
N, K = map(int, input().split())
result = []


def go(n, k):
    if n == 0:
        return
    if DP[n-1] > k:
        result.append(1)
        go(n - 1, k)
    elif DP[n-1] + DP[n-2] > k:
        result.append(2)
        go(n - 2, k - DP[n-1])
    else:
        result.append(3)
        go(n - 3, k - DP[n-1] - DP[n-2])


if DP[N] < K:
    print(-1)
else:
    go(N, K-1)
    print('+'.join(list(map(str, result))))
