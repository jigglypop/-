def permutation(arr, n):
    result = []
    def generate(chosen, used):
        if len(chosen) == n:
            _chosen = chosen[::]
            result.append(_chosen)
            return
        for i in range(len(arr)):
            if not used & (1 << i):
                chosen.append(arr[i])
                generate(chosen, used | (1 << i))
                chosen.pop()
    generate([], 0)
    return result

result = permutation([1,2,3],2)
print(result)
