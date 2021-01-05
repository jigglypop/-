import sys
sys.stdin = open("2003.txt", "r")
N, M = map(int, input().split())
A = list(map(int, input().split()))

left = temp = result = 0
for right in range(N):
    temp += A[right]
    while temp > M:
        temp -= A[left]
        left += 1
    if temp == M:
        result += 1
print(result)
