import sys
from math import ceil, log2
sys.stdin = open('1395.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
H = int(ceil(log2(N)))
A = [0] * (N)
tree = [0] * (1 << (H+1))
lazy = [0] * (1 << (H+1))


for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        update_range()
