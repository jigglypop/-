import sys
sys.stdin = open("17298.txt", "r")
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [0] * N
S = [0]
for i in range(1, N):
    if not S:
        S.append(i)
    while S and A[S[-1]] < A[i]:
        result[S.pop()] = A[i]
    S.append(i)
while S:
    result[S.pop()] = -1
print(' '.join(map(str, result)))
