def solution(n, arr1, arr2):
    result = []
    for a, b in zip(arr1,arr2):
        c = a | b
        result.append(bin(c)[2:])
    len_result = []
    for r in result:
        len_result.append(len(r))
    max_len = max(len_result)
    answer = []
    for r in result:
        blank = max_len - len(r)
        r_replace = r.replace('1','#')
        r_replace = r_replace.replace('0',' ')
        r_replace = " " * blank + r_replace
        answer.append(r_replace)
        
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))