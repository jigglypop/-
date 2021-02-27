from math import floor
import sys
sys.stdin = open('1072.txt', 'r')
input = sys.stdin.readline
X, Y = map(int, input().split())
Z = floor(100 * Y / X)
lo, hi = 0, 1000000000
if Z >= 99:
    print(-1)
else:
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if floor(100 * (Y + mid) / (X + mid)) <= Z:
            lo = mid
        else:
            hi = mid
    print(hi)
