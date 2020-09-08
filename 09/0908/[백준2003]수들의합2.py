import sys
sys.stdin = open("2003.txt", "r")
n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
lo, hi = 0, 1
tmp = arr[lo]
while lo < n:
    if tmp == m:
        cnt += 1
        tmp -= arr[lo]
        lo += 1
    if hi == n and tmp < n:
        break
    elif tmp < m:
        tmp += arr[hi]
        hi += 1
    elif tmp > m:
        tmp -= arr[lo]
        lo += 1
print(cnt)
