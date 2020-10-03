arr = 'ABC'
N = len(arr)
R = 3
chosen = [''] * R


def COMB(arr, r):
    chosen = []

    def comb(k, start):
        if k == r:
            print(chosen)
            return
        for i in range(start, N):
            chosen.append(arr[i])
            comb(k + 1, i + 1)
    comb(0, 0)


COMB(arr, 2)
