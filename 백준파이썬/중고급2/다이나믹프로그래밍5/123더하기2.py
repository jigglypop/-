import sys
sys.setrecursionlimit(100000)
sys.stdin = open('12101.txt', 'r')
input = sys.stdin.readline

DP = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, -1]
N, K = map(int, input().split())
DP[0] = 1
DP[1] = 1
DP[2] = 2
for i in range(3, 11):
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
print(DP)
result = []


def Print(n, k):
    if n == 0:
        return
    if DP[n-1] > k:
        result.append(1)
        Print(n-1, k)
    elif DP[n-2] > k - DP[n-1]:
        result.append(2)
        Print(n-2, k - DP[n-1])
    else:
        result.append(3)
        Print(n-3, k - DP[n-1] - DP[n-2])


if DP[N] < K:
    print(-1)
else:
    Print(N, K-1)
    result = '+'.join(list(map(str, result)))
    print(result)
