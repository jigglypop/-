import sys
sys.stdin = open("9253.txt", "r")
input = sys.stdin.readline

S1 = input()
S2 = input()
P = input()


def kmp(P, S):
    N = len(S)
    M = len(P)
    j = 0
    pi = [0] * M
    for i in range(1, M):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if P[i] == P[j]:
            pi[i] = j + 1
            j += 1
        else:
            pi[i] = 0

    j = 0
    for i in range(N):
        while j > 0 and S[i] != P[j]:
            j = pi[j - 1]
        if S[i] == P[j]:
            if j == M - 1:
                return True
            else:
                j += 1
    return False


print('YES') if kmp(P, S1) and kmp(P, S2) else print('NO')
