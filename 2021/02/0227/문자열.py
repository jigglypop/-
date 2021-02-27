import sys
sys.stdin = open('1120.txt', 'r')
input = sys.stdin.readline
A, B = input().split()
_min = len(A)
for i in range(len(B)-len(A)+1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    if count < _min:
        _min = count

print(_min)
