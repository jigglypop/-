def solution(A):
    A_set = set()
    result = 0
    for a in A:
        if a not in A_set:
            if -a not in A_set:
                result += 1
                A_set.add(a)
    return result


print(solution([-5, -3, -1, 0, 3, 6]))
