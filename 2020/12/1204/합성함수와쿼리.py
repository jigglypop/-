import sys
from math import log2
from pprint import pprint
sys.stdin = open('17435.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
logN = 20
P = [[0] * logN for _ in range(N+1)]
board = list(map(int, input().split()))
for i in range(1, N+1):
    P[i][0] = board[i-1]

for j in range(1, logN):
    for i in range(1, N+1):
        P[i][j] = P[P[i][j-1]][j-1]

for _ in range(int(input())):
    n, x = map(int, input().split())
    for i in range(20):
        if ((n & (1 << i)) > 0):
            x = P[x][i]
    print(str(x) + '\n')
