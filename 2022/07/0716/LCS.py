
from pprint import pprint
import sys
sys.stdin = open('./text/9251.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

A, B = Str(), Str()
Y, X = len(A), len(B)
dp = [[0] * (X + 1) for _ in range(Y + 1)]
for y in range(1, Y + 1):
    for x in range(1, X + 1):
        if A[y - 1] == B[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y][x - 1], dp[y - 1][x])
print(dp[-1][-1])
