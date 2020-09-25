import sys
sys.stdin = open('2343.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

start, end = 0, max(arr)
result = 0
while start <= end:
    mid = (start+end)//2
    max_x = min_x = arr[0]
    cnt = 1
    for i in range(1, n):
        max_x = max(max_x, arr[i])
        min_x = min(min_x, arr[i])
        if max_x - min_x > mid:
            cnt += 1
            max_x = arr[i]
            min_x = arr[i]
    if cnt <= m:
        end = mid-1
        result = mid
    else:
        start = mid+1

print(result)
