def permutation(arr, n):
    result = []
    used = [True for _ in range(len(arr))]
    def generate(chosen, used):
        if len(chosen) == n:
            _chosen = chosen[::]
            result.append(_chosen)
            return
        for i in range(len(arr)):
            if used[i]:
                chosen.append(arr[i])
                used[i] = False
                generate(chosen, used)
                used[i] = True
                chosen.pop()
    generate([], used)
    return result

result = permutation([1,2,3],2)
print(result)
