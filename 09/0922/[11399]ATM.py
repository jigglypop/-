import sys
sys.stdin = open('11399.txt', 'r')

N = int(input())
p = list(map(int, input().split()))
P = []
for key, value in enumerate(p):
    P.append((key+1, value))
P = sorted(P, key=lambda x: x[1])
print(P)
