import sys
sys.stdin = open('1234.txt', 'r')
input = sys.stdin.readline
N, R, G, B = map(int, input().split())
DP = [[[[-1] * (B+1) for _ in range(G+1)] for _ in range(R+1)]
      for _ in range(N+1)]
Comb = [[0] * 11 for _ in range(11)]
Comb[0][0] = 1
for i in range(1, 11):
    Comb[i][0] = 1
    Comb[i][i] = 1
    for j in range(1, i):
        Comb[i][j] = Comb[i-1][j-1] + Comb[i-1][j]


def go(n, r, g, b):
    if r < 0 or g < 0 or b < 0:
        return 0
    if n == 0:
        return 1
    if DP[n][r][g][b] != -1:
        return DP[n][r][g][b]
    DP[n][r][g][b] = 0
    DP[n][r][g][b] += go(n - 1, r - n, g, b)
    DP[n][r][g][b] += go(n - 1, r, g - n, b)
    DP[n][r][g][b] += go(n - 1, r, g, b - n)
    if n % 2 == 0:
        DP[n][r][g][b] += go(n - 1, r - n // 2, g - n // 2, b) * Comb[n][n//2]
        DP[n][r][g][b] += go(n - 1, r, g - n // 2, b - n // 2) * Comb[n][n//2]
        DP[n][r][g][b] += go(n - 1, r - n // 2, g, b - n // 2) * Comb[n][n//2]
    if n % 3 == 0:
        DP[n][r][g][b] += go(n - 1, r - n // 3, g - n // 3,
                             b - n // 3) * Comb[n][n//3] * Comb[n-n//3][n//3]

    return DP[n][r][g][b]


print(go(N, R, G, B))
