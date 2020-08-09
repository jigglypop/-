def LPS(pat, lps):
    leng = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1


def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    LPS(pat, lps)
    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif txt[i] != pat[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]


# 조금 더 긴 텍스트
# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
# 본문에서 다룬 예제
txt = 'ABXABABXAB'
pat = 'ABXAB'
KMP(pat, txt)
