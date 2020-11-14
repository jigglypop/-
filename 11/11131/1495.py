import sys
from pprint import pprint
sys.stdin = open("1495.txt", "r")
input = sys.stdin.readline

N, S, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[0] * (M+1) for _ in range(N+1)]
DP[0][S] = 1
for j in range(N):
    for i in range(M+1):
        if DP[j][i] == 1:
            a = i + A[j+1]
            b = i - A[j+1]
            if 0 <= a <= M:
                DP[j+1][a] = 1
            if 0 <= b <= M:
                DP[j+1][b] = 1
result = -1
for i in range(M, -1, -1):
    if DP[N][i] == 1:
        result = max(result, i)
print(result)
