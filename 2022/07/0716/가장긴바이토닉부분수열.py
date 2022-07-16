import operator
import sys
sys.stdin = open('./text/11054.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
A = list(Split())
dpA = [1] * N
dpB = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and dpA[i] <= dpA[j]:
            dpA[i] = dpA[j] + 1

for i in reversed(range(N)):
    for j in range(i, N):
        if A[i] > A[j] and dpB[i] <= dpB[j]:
            dpB[i] = dpB[j] + 1

print(int(max(map(operator.add, dpA, dpB)) - 1))
