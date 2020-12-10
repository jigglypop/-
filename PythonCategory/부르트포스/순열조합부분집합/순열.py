from pprint import pprint


def PERM(arr, r):
    result = []
    used = [0 for _ in range(len(arr))]

    def perm(k, chosen, used):
        if k == r:
            # 파이썬은 포인터값을 저장하기 때문에 참조 원본이 바뀌면 복사해서 넣어주어야 함
            result.append(chosen[::])
            return
        for i in range(len(arr)):
            if used[i]:
                continue
            chosen.append(arr[i])
            used[i] = 1
            perm(k+1, chosen, used)
            used[i] = 0
            chosen.pop()
    perm(0, [], used)
    return result


result = PERM('ABCDE', 3)
pprint(result)
pprint(str(len(result)) + "개")
