from bisect import *

A = [2, 2, 3, 3, 4, 5]
lo, hi = -1, len(A)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if A[mid] < 3:
        lo = mid
    else:
        hi = mid
print(hi)