def permutations(arr, r):
    R = []
    used = [0 for _ in range(len(arr))]
    def perm(k, chosen, used):
        if k == r:
            copy = chosen[::]
            R.append(copy)
            return
        for i in range(len(arr)):
            chosen.append(arr[i])
            used[i] = 1
            perm(k+1, chosen, used)
            used[i] = 0
            chosen.pop()
    perm(0, [], used)
    return R
print(permutations('ABCDE',2))