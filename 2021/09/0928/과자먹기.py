import sys
sys.stdin = open("./text/16401.txt", "r")
input = sys.stdin.readline
M, N = map(int, input().split())
nums = list(map(int, input().split()))
lo, hi = 0, max(nums) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    counts = 0
    for num in nums:
        counts += num // mid
    if counts >= M:
        lo = mid
    else:
        hi = mid
print(lo)
