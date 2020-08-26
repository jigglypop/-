def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    before, after = [], []
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            before.append(arr[i])
        else:
            after.append(arr[i])
    return quicksort(before) + [pivot] + quicksort(after)


print(quicksort([3, 1, 4, 5, 2]))
