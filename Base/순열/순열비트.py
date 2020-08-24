from pprint import pprint


def PERM(arr, r):
    result = []

    def perm(k, chosen, used):
        if k == r:
            result.append(chosen[::])
            return
        for i in range(len(arr)):
            if used & (1 << i):
                continue
            chosen.append(arr[i])
            perm(k+1, chosen, used | (1 << i))
            chosen.pop()

    perm(0, [], 0)
    return result


result = PERM('ABC', 2)
pprint(result)
pprint(str(len(result)) + "개")
