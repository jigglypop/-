def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    before = mergesort(nums[:mid])
    after = mergesort(nums[mid:])
    result = []
    while before and after:
        if before[0] < after[0]:
            result.append(before.pop(0))
        else:
            result.append(after.pop(0))
    return result + before + after


print(mergesort([3, 1, 4, 5, 2]))
