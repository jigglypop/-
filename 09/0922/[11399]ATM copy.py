import sys
sys.stdin = open('11399.txt', 'r')

N = int(input())
P = list(map(int, input().split()))
P.sort()
result = 0
for i in range(N-1):
    P[i+1] += P[i]
print(sum(P))
