import sys
sys.stdin = open('10942.txt', 'r')
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
DP = [[0] * N for _ in range(N)]
for i in range(N):
    DP[i][i] = 1
for i in range(N-1):
    if A[i] == A[i+1]:
        DP[i][i+1] = 1
for k in range(2, N):
    for i in range(0, N-k):
        j = i + k
        if A[i] == A[j] and DP[i+1][j-1] == 1:
            DP[i][j] = 1
for _ in range(int(input())):
    S, E = map(int, input().split())
    print(DP[S-1][E-1])
