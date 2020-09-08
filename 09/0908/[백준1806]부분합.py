import sys
sys.stdin = open("1806.txt", "r")

N, S = map(int, input().split())
A = list(map(int, input().split()))

sums = [0] * (N + 1)
for i in range(1, N + 1):
    sums[i] = sums[i-1] + A[i-1]

result = 1000001
left = 0
for right in range(1, N+1):
    while left < right and sums[right] - sums[left] >= S:
        result = min(result, right-left)
        left += 1
    if sums[right] - sums[left] < S:
        left == 0
print(result) if result != 1000001 else print(0)
