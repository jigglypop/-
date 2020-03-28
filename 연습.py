def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    low = merge(arr[:mid])
    high = merge(arr[mid:])
    buff = []
    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            buff.append(low[l])
            l += 1
        else:
            buff.append(high[h])
            h += 1
    buff += low[l:]
    buff += high[h:]
    return buff





arr = [1, 4, 3, 5, 2, 6, 8, 7, 9, 7]
print(merge(arr))