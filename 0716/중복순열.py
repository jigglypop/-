def combinations(arr, r):
    for i in range(len(arr)):  # 함수에서 지금할 일
        if r == 1:  # 종료조건
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):  # 다음에 할 일
                yield [arr[i]] + next


#  아래는 함수를 실행하기 위한 사용법입니다.
for combi in combinations([1, 2, 3, 4, 5], 2):
    print(combi)
