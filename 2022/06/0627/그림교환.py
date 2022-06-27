import sys
sys.stdin = open("./text/1029.txt", "r")
input = sys.stdin.readline
N = int(input())
A = [[*map(int, list(input().strip()))] for _ in range(N)]
dp = [[[0] * 10 for _ in range(N)] for _ in range(1 << N)]

for a in A[0]:
    if a != 0:
        dp[1][0][a] = 1
#    상태  지금사람 지금가격
# dp[state][i][cost]
for state in range(1 << N):
    for i in range(1, N):
        if state & (1 << i):
            print(i, state)
            for cost in range(10):
                for j in range(1, N):
                    if i != j and state & (1 << j) and dp[state - (1 << i)][j][cost] != 0 and cost <= A[i][j]:
                        print(i, j)
                        dp[state][i][A[i][j]] = max(dp[state][i][A[i][j]], dp[state | j - (1 << i)][j][cost] + 1)

print(dp)
print(9 - 8)