def computeLPS(pat, lps):
    leng = 0  # 이전 접미어와 접두어의 최대 길이
    # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    i = 1
    while i < len(pat):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            # 일치하지 않는 경우
            if leng != 0:
                # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
                leng = lps[leng-1]
                # 다시 검사해야 하므로 i는 증가하지 않음
            else:
                # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                lps[i] = 0
                i += 1
    return pat, lps


pat = 'ABXAB'
lps = [0,0,0,0,0]
print(computeLPS(pat,lps))
