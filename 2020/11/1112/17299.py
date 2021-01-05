import sys
from collections import Counter
sys.stdin = open('17299.txt', 'r')

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
count = Counter(A)
ans = [0] * N
S = [0]
for i in range(1, N):
    if not S:
        S.append(i)
    while S and count[A[S[-1]]] < count[A[i]]:
        ans[S.pop()] = A[i]
    S.append(i)
while S:
    ans[S.pop()] = -1
print(" ".join(map(str, ans)))
