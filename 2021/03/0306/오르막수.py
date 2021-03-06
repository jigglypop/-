import sys
from pprint import pprint
sys.stdin = open('11057.txt', 'r')
input = sys.stdin.readline
N = int(input())
DP = [[0] * 10 for _ in range(N)]
for i in range(10):
    DP[0][i] = 1
for y in range(1, N):
    for x in range(10):
        for z in range(x+1):
            DP[y][x] += DP[y-1][z] % 10007
print(sum(DP[-1]))
