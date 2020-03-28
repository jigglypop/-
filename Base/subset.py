def subset(arr):
    result = []
    for i in range(1 << len(arr)):
        _result = []
        for j in range(len(arr)+1):
            if i & (1 << j):
                _result.append(arr[j])
        result.append(_result)
    return result
result = subset([1,2,3])
print(result)