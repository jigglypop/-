
def solution(A):
    result = 0
    N = len(A)
    check = [False] * (N+1)
    for a in A:
        if 1 <= a < N+1:
            check[a] = True
        else:
            return 0
    for i in range(1, N+1):
        if check[i] == False:
            return 0
    return 1


print(solution([4, 1, 3]))
