import sys
from pprint import pprint
sys.stdin = open("1102.txt", "r")
INF = sys.maxsize
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
plants = input()
count = plants.count('Y')
S = int('0b' + plants.replace('Y', '1').replace('N', '0')[::-1], 2)

P = int(input())
DP = [-1 for _ in range(1 << 16)]
DP[S] = 0
for i in range(1 << N):
    if DP[i] == -1:
        continue
    for j in range(N):
        if i & (1 << j):
            for k in range(N):
                if not (i & (1 << k)):
                    if DP[i | (1 << k)] == -1 or DP[i | (1 << k)] > DP[i] + board[j][k]:
                        DP[i | (1 << k)] = DP[i] + board[j][k]
result = -1
for i in range(1 << N):
    if DP[i] == -1:
        continue
    count = 0
    for j in range(N):
        if i & (1 << j):
            count += 1
    if count >= P:
        if result == -1 or result > DP[i]:
            result = DP[i]
print(result)
