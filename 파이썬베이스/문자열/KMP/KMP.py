def LPS(pat):
    lps = [0] * len(pat)
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]:
            j = lps[j - 1]
        if pat[i] == pat[j]:
            j += 1
            lps[i] = j
        else:
            lps[i] = 0
    return lps


def kmp(txt, pat):
    lps = LPS(pat)
    P = len(pat)
    j = 0
    result = []
    for i in range(len(txt)):
        while j > 0 and txt[i] != pat[j]:
            j = lps[j-1]
        if txt[i] == pat[j]:
            if j == P - 1:
                result.append(i - P + 1)
                j = lps[j]
            else:
                j += 1
    return result


txt = 'ABXABABYABCDE'
pat = 'ABYAB'
print(kmp(txt, pat))
