def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    before = mergesort(arr[:mid])
    after = mergesort(arr[mid:])
    result = []
    while before and after:
        if before[0] < after[0]:
            result.append(before.pop(0))
        else:
            result.append(after.pop(0))
    return result + before + after


print(mergesort([3, 1, 4, 5, 2]))
