import sys
from math import log

sys.stdin = open('1790.txt', 'r')

N, K = map(int, input().split())


def calc(N):
    count = 0
    logN = int(log(N, 10))+1
    for i in range(1, logN+1):
        Max = min(10**i-1, N)
        Min = 10**(i-1) - 1
        count += (Max - Min) * i
    return count


if calc(N) < K:
    print(-1)
    sys.exit(0)
start, end = 1, N
result = 0
while start <= end:
    mid = (start + end) // 2
    count = calc(mid)
    if count < K:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
gap = calc(result) - K
lens = len(str(result))
print(str(result)[lens-gap-1])
