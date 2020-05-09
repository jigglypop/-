def permutations(arr, r):
    N = len(arr)
    R = []
    def perm(k, used,chosen):
        if k == r:
            copy = chosen[::]
            R.append(copy)
            return
        for i in range(N):
            if used & (1 << i): continue
            chosen.append(arr[i])
            perm(k + 1, used | (1 << i),chosen)
            chosen.pop()
    perm(0,0,[])
    return R


print(permutations('ABCDE', 2))

