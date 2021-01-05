import sys
from pprint import pprint
sys.stdin = open('9252.txt', 'r')
input = sys.stdin.readline
# A = list(input())
# B = list(input())
# DP = [[""] * (len(B) + 1) for _ in range(len(A) + 1)]
# for y in range(1, len(A) + 1):
#     for x in range(1, len(B) + 1):
#         if A[y - 1] == B[x - 1]:
#             DP[y][x] = DP[y - 1][x - 1] + A[y - 1]
#         else:
#             if len(DP[y - 1][x]) >= len(DP[y][x - 1]):
#                 DP[y][x] = DP[y - 1][x]
#             else:
#                 DP[y][x] = DP[y][x - 1]

# if len(DP[-1][-1]) == 0:
#     print(0)
# else:
#     print(len(DP[-1][-1]))
#     print(DP[-1][-1])
input = sys.stdin.readline
A = input()
B = input()
X = len(A)
Y = len(B)
DP = [[''] * (X + 1) for _ in range(Y + 1)]
for y in range(Y):
    for x in range(X):
        if A[x] == B[y]:
            DP[y+1][x+1] = DP[y][x] + A[x]
        else:
            if len(DP[y][x+1]) >= len(DP[y+1][x]):
                DP[y+1][x+1] = DP[y][x+1]
            else:
                DP[y+1][x+1] = DP[y+1][x]
if len(DP[-1][-1]) == 0:
    print(0)
else:
    print(len(DP[-1][-1]))
    print(DP[-1][-1])