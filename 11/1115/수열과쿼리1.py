import sys
from math import ceil, log2
sys.stdin = open('13537.txt', 'r')

N = int(input())
tree = [0] * (N+1)


def update(tree, x, i):
    while i < len(tree):
        tree[i] = x
        i += (i & -i)


A = [0] + list(map(int, input().split()))
for i in range(1, N):
    update(tree, A[i], i)
print(tree)
M = int(input())
for _ in range(M):
    temp = list(map(int, input().split()))
