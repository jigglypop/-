import sys
sys.stdin = open("2776.txt", "r")
input = sys.stdin.readline


def lower_bound(A, b):
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] < b:
            start = mid + 1
        elif A[mid] == b:
            return 1
        else:
            end = mid - 1
    return 0


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    M = int(input())
    B = list(map(int, input().split()))
    for b in B:
        print(lower_bound(A, b))
