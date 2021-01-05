import sys
from math import ceil, log2
sys.stdin = open('1328.txt', 'r')

DP = [[[0] * 101 for _ in range(101)] for _ in range(101)]
N, L, R = map(int, input().split())
print(N, L, R)
