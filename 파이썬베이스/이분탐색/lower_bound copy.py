import sys

# 1 2 3 4 4 4 5 6 7 8
M = 4
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
lo, hi = 0, 10
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if M >= nums[mid]:
        lo = mid
    else:
        hi = mid
print(hi)
