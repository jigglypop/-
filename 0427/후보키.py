from itertools import chain, combinations


def get_all_subset(iterable):
    s = list(iterable)
    d = chain.from_iterable(combinations(iterable, r)
                            for r in range(len(iterable) + 1))
    return d


def solution(relation):
    answer_list = []
    subset_list = get_all_subset(list(range(0, len(relation[0]))))
    unique_list = []
    for subset in subset_list:
        unique = True
        row_set = set()
        for row in range(len(relation)):
            data = ''
            for column in subset:
                data += relation[row][column] + '.'
            if data in row_set:
                unique = False
                break
            row_set.add(data)

        if unique:
            unique_list.append(subset)

    unique_list = sorted(unique_list, key=lambda x: len(x))

    for subset in unique_list:
        subset = set(subset)
        check = True
        for j in answer_list:
            if j.issubset(subset):
                check = False
        if check == True:
            answer_list.append(subset)
    return len(answer_list)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
    "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
