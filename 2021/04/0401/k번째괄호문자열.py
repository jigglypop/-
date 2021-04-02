import sys
sys.stdin = open("17428.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
DP = [[0] * (N+1) for _ in range(N+1)]
DP[0][0] = 1
for i in range(1, N+1):
    DP[0][i] = 0
for i in range(1, N+1):
    DP[i][0] = DP[i-1][1]
    for j in range(1, N+1):
        DP[i][j] = DP[i-1][j-1]
        if j+1 <= N:
            DP[i][j] += DP[i-1][j+1]

if K >= DP[N][0]:
    print(-1)
    exit()
op = 0
for i in range(N, 0, -1):
    if op == 0:
        print('(', end='')
        op += 1
    else:
        if K < DP[i-1][op+1]:
            print('(', end='')
            op += 1
        else:
            print(')', end='')
            K -= DP[i-1][op+1]
            op -= 1
print()
