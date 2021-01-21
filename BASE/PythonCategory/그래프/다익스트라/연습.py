def solutions(S, C):
    word_dict = dict({S[0]: [C[0]]})
    flag = S[0]
    for i in range(1, len(S)):
        if S[i] == flag:
            word_dict[S[i]].append(C[i])
        else:
            flag = S[i]
            word_dict[S[i]] = [C[i]]
    result = 0
    for key, value in word_dict.items():
        result += sum(value) - max(value)
    return result


print(solutions('abccbd', [0, 1, 2, 3, 4, 5]))
print(solutions('aabbcc', [1, 2, 1, 2, 1, 1, 1, 1, 2]))
print(solutions('aaaa', [3, 4, 5, 6]))
print(solutions('ababa', [10, 5, 10, 5, 10]))
