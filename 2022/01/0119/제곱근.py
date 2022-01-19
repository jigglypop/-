import sys
sys.stdin = open("./text/13706.txt", "r")
input = sys.stdin.readline
N = int(input())
lo, hi = 0, N
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if mid ** 2 <= N:
        lo = mid
    else:
        hi = mid
print(lo)
