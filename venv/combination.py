def combination(arr, n):
    result = []
    def generate(chosen, start):
        if len(chosen) == n:
            _chosen = chosen[::]
            result.append(_chosen)
            return
        for i in range(start,len(arr)):
            chosen.append(arr[i])
            generate(chosen, i + 1)
            chosen.pop()
    generate([],0)
    return result
result = combination([1,2,3,4],2)
print(result)
