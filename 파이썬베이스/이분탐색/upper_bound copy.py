import sys
# sys.stdin = open('이진탐색.txt', 'r')

# 1 2 3 4 4 4 5 6 7 8
N, M = 10, 3
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8]
start, end = 0, N-1
result = 0
while start <= end :
    mid = (start + end) // 2
    temp = nums[mid]
    # 여기
    if temp < M + 2:
        start = mid + 1
    else:
        # 여기
        result = mid
        end = mid - 1
print(result)
