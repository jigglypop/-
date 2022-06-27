import sys
sys.stdin = open("./text/1029.txt", "r")
input = sys.stdin.readline
N = int(input())
A = [[*map(int, list(input().strip()))] for _ in range(N)]
dp = [[[-1] * 10 for _ in range(N)] for _ in range(1 << N)]
M = (1 << N) - 1
def go(state, i, cost):
    ret = dp[state][i][cost]
    if ret != -1:
        return ret
    dp[state][i][cost] = 1
    for j in range(N):
        if not state & (1 << j) and cost <= A[i][j] and i != j:
            dp[state][i][cost] = max(dp[state][i][cost], go(state | (1 << j), j, A[i][j]) + 1)
    return dp[state][i][cost]
            
for a in A[0]:
    go(1, 0, a)
print(max(dp[1][0]))