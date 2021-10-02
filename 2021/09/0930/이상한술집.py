import sys
sys.stdin = open("./text/13702.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
lo, hi = 0, max(nums) + 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    temp = 0
    for num in nums:
        temp += num // mid
    if temp >= K:
        lo = mid
    else:
        hi = mid
print(lo)
