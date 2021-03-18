import sys
sys.stdin = open('이진탐색.txt', 'r')

# 1 2 3 4 4 4 5 6 7 8
N, M = map(int, input().split())
nums = list(map(int, input().split()))
start, end = 0, N-1
while start <= end:
    mid = (start + end) // 2
    temp = nums[mid]
    if temp <= M:
        start = mid + 1
    else:
        end = mid - 1
print(start)
