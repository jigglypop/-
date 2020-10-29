import sys
sys.stdin = open("1806.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

left = right = 0
Min = N+1
Sum = A[0]
while left <= right and right < N:
    if Sum < M:
        right += 1
        if right < N:
            Sum += A[right]
    elif Sum == M:
        Min = min(Min, right + 1 - left)
        right += 1
        if right < N:
            Sum += A[right]
    elif Sum > M:
        Min = min(Min, right + 1 - left)
        Sum -= A[left]
        left += 1
        if left > right and left < N:
            left = right
            Sum -= A[left]
print(Min if Min <= N else 0)
