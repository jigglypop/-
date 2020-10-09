nums = [1, 2, 3]
result = []


def subset(index, path):
    result.append(path)
    for i in range(index, len(nums)):
        subset(i+1, path+[nums[i]])


subset(0, [])
print(result)
