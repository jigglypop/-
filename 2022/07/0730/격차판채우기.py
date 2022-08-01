import sys
sys.stdin = open('./text/1648.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M = Split()
dp = [[0] * (1 << M) for _ in range(N * M + 1)]
dp[N * M][0] = 1
for num in reversed(range(N * M)):
    for state in range(1 << M):
        if state & 1:
            dp[num][state] = dp[num + 1][state >> 1]
        else:
            if num < (N - 1) * M:
                dp[num][state] += dp[num + 1][(1 << (M - 1)) | (state >> 1)]
            if num % M != M-1 and not state & 2:
                dp[num][state] += dp[num + 2][state >> 2]
print(dp[0][0] % 9901)