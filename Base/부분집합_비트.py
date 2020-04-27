
def subset(arr):
    N = len(arr)
    chosen = []

    def sub(k, n, bits):
        if k == n:
            result = []
            for i in range(N):
                if bits & 1 << i:
                    result.append(arr[i])
            chosen.append(result)
            return
        sub(k+1, n, bits | 1 << k)
        sub(k+1, n, bits)
    sub(0, N, 0)
    return chosen


print(subset('ABC'))
