import sys
from pprint import pprint
sys.stdin = open('9252.txt', 'r')
input = sys.stdin.readline
A = input()
B = input()
X = len(A)
Y = len(B)
DP = [[0] * (X + 1) for _ in range(Y + 1)]
result = 0
for y in range(Y):
    for x in range(X):
        if A[x] == B[y]:
            DP[y+1][x+1] = DP[y][x] + 1
            result = max(result, DP[y+1][x+1])
        else:
            DP[y+1][x+1] = max(DP[y][x+1], DP[y+1][x])
print(result)
