import sys
from math import log

sys.stdin = open('1790.txt', 'r')

n, k = map(int, input().split())

ans = 0


def count(n):
    ans = 0
    start = 1
    len = 1
    while start <= n:
        end = start * 10-1
        if end > n:
            end = n
        ans += (end-start+1)*len
        start *= 10
        len += 1
    return ans


if count(n) < k:
    print(-1)
    sys.exit(0)
start = 1
end = n
ans = 0
while (start <= end):
    mid = (start + end) // 2
    len_num = count(mid)
    if (len_num < k):
        start = mid+1
    else:
        ans = mid
        end = mid-1
s = str(ans)
l = count(ans)
idx = len(s)-(l-k)-1
print(s[idx])
