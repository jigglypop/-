import sys
from collections import Counter
sys.stdin = open("2143.txt", "r")
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
first = []
second = []
for i in range(N):
    Sum = 0
    for j in range(i, N):
        Sum += A[j]
        first.append(Sum)
for i in range(M):
    Sum = 0
    for j in range(i, M):
        Sum += B[j]
        second.append(Sum)
first.sort()
second.sort()
counter = Counter(second)
result = 0
for num in first:
    result += counter[T - num]
print(result)
