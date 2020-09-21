from pprint import pprint


def PERM(arr, r):
    result = []

    def perm(k, choice, used):
        if k == r:
            result.append(choice[::])
            return
        for i in range(len(arr)):
            if used & (1 << i):
                continue
            choice.append(arr[i])
            perm(k+1, choice, used | (1 << i))
            choice.pop()
    perm(0, [], 0)
    return result


result = PERM('ABCDE', 3)
pprint(result)
pprint(str(len(result)) + "개")
