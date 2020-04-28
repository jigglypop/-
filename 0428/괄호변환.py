def check(word):
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) > 0:
        return False
    return True


def word_split(word_all):
    good = []
    bad = []
    for i in range(1, len(word_all)):
        if i == len(word_all)-1:
            bad.append(word_all)
        if check(word_all[:i]):
            good.append(word_all[:i])
            if check(word_all[i:]):
                good.append(word_all[i:])
            else:
                bad.append(word_all[i:])
            break
    return good, bad


def solution(word):
    good, bad = word_split(word)
    print(good)
    print(bad)
    answer = 0
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
