from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/13576.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

S = input()
N = len(S)
Z = [0] * N
L = R = 0
for i in range(1, N):
    L = R = 0
    if i <= R:
        Z[i] = min(R - i + 1, Z[i - L])
    while i + Z[i] < N and S[i + Z[i]] == S[Z[i]]:
        Z[i] += 1   
    if R < i + Z[i] - 1:
        R  = i + Z[i] - 1
        L = i
print(Z)