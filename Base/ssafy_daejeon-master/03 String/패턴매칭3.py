p = "CATTCCCTGCGCCGC"
# pattern (m, j)                                                                     
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      
# text (n, i)

# 3. Brute-Force2
m, n = len(p), len(t)
i = j = 0
while i < n:
    if p[j] != t[i]:
        i -= j           # j까지 했던것 빼주고 다시시작
        j = -1           # 일치하지 않으므로 전의 것으로 돌아감
    i, j = i + 1, j + 1
    if j == m:
        print(t[i- j:])
        break