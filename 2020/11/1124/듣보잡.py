import sys
from pprint import pprint
sys.stdin = open('1764.txt', 'r')

N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]
C = list(set(A) & set(B))
C.sort()
print(len(C))
for c in C:
    print(c)
