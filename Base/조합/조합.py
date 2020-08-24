from pprint import pprint


def COMB(arr, r):
    result = []

    def comb(k, chosen, start):
        if k == r:
            result.append(chosen[::])
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            comb(k+1, chosen, i+1)
            chosen.pop()
    comb(0, [], 0)
    return result


result = COMB('ABCDE', 2)
pprint(result)
pprint(str(len(result)) + "개")
