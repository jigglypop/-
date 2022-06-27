for state in range(1 << N):
#     for i in range(N):
#         if state & (1 << i):
#             for j in range(N):
#                 if i != j and dp[state | (1 << j)][j] <= A[j][i]:
#                     dp[state][i]  = max(dp[state][i], dp[state | (1 << j)][j] + 1)