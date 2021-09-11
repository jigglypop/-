def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    before = merge(arr[:mid])
    after = merge(arr[mid:])
    result = []
    while before and after:
        if before[0] < after[0]:
            result.append(before.pop(0))
        else:
            result.append(after.pop(0))
    return result + before + after


print(merge([3, 1, 4, 5, 2]))
