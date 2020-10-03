import sys
sys.stdin = open('16916.txt', 'r')
s = str(input())
p = str(input())


def preprocessing(p):
    m = len(p)
    pi = [0] * m
    pi[0] = 0
    j = 0
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            pi[i] = j + 1
            j += 1
        else:
            pi[i] = 0
    return pi


def kmp(s, p):
    pi = preprocessing(p)
    n = len(s)
    m = len(p)
    j = 0
    ans = []
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i - m + 1)
            else:
                j += 1
    return ans


txt = 'ABXABABXAB'
pat = 'ABXAB'
print(kmp(pat, txt))
