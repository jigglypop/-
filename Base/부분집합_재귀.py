
def subset(arr):
    N = len(arr)
    bits = [0] * N
    chosen = []

    def sub(k, n):
        if k == n:
            result = []
            for i in range(N):
                if bits[i]:
                    result.append(arr[i])
            chosen.append(result)
            return
        bits[k] = 0
        sub(k+1, n)
        bits[k] = 1
        sub(k+1, n)
    sub(0, N)
    return chosen


print(subset('ABC'))
