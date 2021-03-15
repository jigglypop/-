import sys
sys.stdin = open("14719.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
H = list(map(int, input().split()))
A = [0] * X
d = Y
for i in range(X):
    d = min(d, Y-H[i])
    A[i] = d
d = Y
for i in range(X-1, -1, -1):
    d = min(d, Y-H[i])
    A[i] = max(A[i], d)
print(Y * X - sum(H) - sum(A))
