import sys
sys.stdin = open('11048.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[0] * (M+1)] + [[0] + list(map(int, input().split()))
                     for _ in range(N)]
DP = [[0] * (M+1) for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, M+1):
        DP[y][x] = max(DP[y-1][x], DP[y][x-1]) + A[y][x]
print(DP[N][M])
