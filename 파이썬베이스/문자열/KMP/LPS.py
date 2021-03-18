def LPS(pat):
    lps = [0] * len(pat)
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
    return pat, lps


pat = 'ABXAA'
print(LPS(pat))
