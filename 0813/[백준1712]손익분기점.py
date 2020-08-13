import sys
import math
sys.stdin = open('[백준1712]손익분기점.txt', 'r')

A, B, C = map(int, input().split())
x = A / (C - B)
if x < 0:
    print(-1)
else:
    print(math.ceil(x + 1))
