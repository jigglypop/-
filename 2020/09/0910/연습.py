result = []
def comb(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in comb(arr[i+1:], r-1):
                yield [arr[i]] + next
for i in comb(arr, r):
    result.append(i)
print(result)