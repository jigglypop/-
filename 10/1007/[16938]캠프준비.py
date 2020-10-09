import sys
from pprint import pprint
sys.stdin = open('16938.txt', 'r')

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = 0


def subset(index, chosen):
    global result
    if sum(chosen) >= L and sum(chosen) <= R and chosen[-1] - chosen[0] >= X:
        result += 1
    for i in range(index, len(A)):
        subset(i+1, chosen + [A[i]])


subset(0, [])
print(result)
