import sys
from math import ceil
sys.stdin = open('2875.txt', 'r')

input = sys.stdin.readline
N, M, K = map(int, input().split())
cnt = 0
while M + N >= K and N >= 0 and M >= 0:
    N -= 2
    M -= 1
    cnt += 1
print(cnt - 1)
