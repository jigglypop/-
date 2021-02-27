import sys
sys.stdin = open('2417.txt', 'r')
N = int(input())
lo, hi = 0, N
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if mid ** 2 < N:
        lo = mid
    else:
        hi = mid
print(hi)
