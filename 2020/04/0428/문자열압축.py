def word_split(word, n):
    Q = [['1']]
    for i in range(0, len(word), n):
        if word[i:i+n] != Q[-1][0]:
            Q.append([word[i:i+n]])
        else:
            Q[-1].append(word[i:i+n])
    Q = Q[1:]
    result = ''
    for q in Q:
        if len(q) == 1:
            result += q[0]
        else:
            result += str(len(q)) + q[0]
    return len(result)


def solution(s):
    answer = 1001
    N = len(s)//2
    for i in range(1, N+2):
        answer = min(answer, word_split(s, i))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
