import sys
sys.stdin = open("./text/17266.txt", "r")
input = sys.stdin.readline
N, M = int(input()), int(input())
nums = [0] + list(map(int, input().split())) + [N]
lo, hi = 0, N + 1
res = 0
def check(m):
    if nums[1]- nums[0] > m:
        return 0
    if nums[-1]- nums[-2] > m:
        return 0
    for i in range(1, len(nums)-2):
        if (nums[i+1]-nums[i])/2 > m:
            return 0
    return 1
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if not check(mid):
        lo = mid
    else:
        hi = mid
print(hi)
