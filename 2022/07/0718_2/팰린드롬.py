from pprint import pprint
import sys
sys.stdin = open('./text/11046.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(str, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
n = Int()
s = List()
S = ["@"] * (len(s) * 2 + 1)
for i in range(n):
    S[2 * i + 1] = s[i]
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

for _ in range(Int()):
    a, b = Split()
    a -= 1
    b -= 1
    if A[a + b + 1] >= b - a + 1:
        print(1)
    else:
        print(0)
