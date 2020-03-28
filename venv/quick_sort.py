def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, equal, greater = [], [], []
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick(less) + equal + quick(greater)


arr = [1,4,3,5,2,6,8,7,7]
print(quick(arr))