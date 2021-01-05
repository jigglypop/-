import sys
sys.stdin = open("16938.txt","r")
input = sys.stdin.readline

N,L,R,X = map(int,input().split())
A = list(map(int,input().split()))
result = []
count = 0
for i in range(1 << N):
    Min = sys.maxsize
    Max = 0
    Sum = 0
    for j in range(N):
        if i & (1 << j):
            Min = min(Min, A[j])
            Max = max(Max, A[j])
            Sum += A[j]
    if Max - Min >= X and L <= Sum <= R:
        count += 1

print(count)
