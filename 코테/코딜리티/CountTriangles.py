from itertools import combinations


# def solution(A):
#     A.sort()
#     N = len(A)
#     result = 0
#     for x in range(N - 1):
#         z = x + 2
#         for y in range(x + 1, N - 1):
#             while z < N and A[x] + A[y] > A[z]:
#                 z += 1
#             result += z - y - 1
#     return result
def solution(A):
    A.sort()
    result = 0
    for i in range(0, len(A)-2):
        left = i + 1
        right = i + 2
        while right < len(A):
            if A[i] + A[left] > A[right]:
                result += right - left
                right += 1
            elif left < right - 1:
                left += 1
            else:
                right += 1
                left += 1
    return result


print(solution([10, 2, 5, 1, 8, 12]))
