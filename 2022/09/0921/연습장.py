import sys
input = sys.stdin.readline
while True:
    A = list(map(int, input().split()))
    if A[0] == 0: break
    N = 1
    for i in range(A[0]):
        B = A[2 * i + 1]
        C = A[2 * i + 2]
        N = N * B - C
    print(N)