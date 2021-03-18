def kmp(P, S):
    N = len(S)
    M = len(P)
    pi = [0] * N
    pi[0] = 0
    j = 0
    for i in range(1, M):
        while j > 0 and P[j] != P[i]:
            j = pi[j - 1]
        if P[j] == P[i]:
            pi[i] = j + 1
            j += 1
        else:
            pi[i] = 0

    j = 0
    result = []
    for i in range(N):
        while j > 0 and P[j] != S[i]:
            j = pi[j - 1]
        if P[j] == S[i]:
            if j == M - 1:
                result.append(i - (M - 1))
                j = pi[j - 1]
            else:
                j += 1
    return result


P = 'ABXAB'
S = 'ABXABABXAB'

print(kmp(P, S))
