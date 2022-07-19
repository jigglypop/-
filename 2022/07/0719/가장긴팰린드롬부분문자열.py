from pprint import pprint
import sys
from collections import deque
sys.stdin = open('./text/13275.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
S = "@" + "@".join(Str()) + "@"
N = len(S)
A = [0] * N
r = c = -1
Max = 0
for i in range(1, N):
    if i <= r:
        A[i] = min(r - i, A[2 * c - i])
    else:   
        A[i] = 0
    while i + A[i] + 1 < N and S[i - (A[i] + 1)] == S[i + (A[i] + 1)]:
        A[i] += 1
    if r < i + A[i]:
        r = i + A[i]
        c = i
    Max = max(A[i], Max)
print(Max)
