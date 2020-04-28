p = "CATTCCCTGCGCCGC"                                                                       # pattern
# m, j 
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text
# n, i

# 2. Brute-Force1
m, n = len(p), len(t)
for i in range(n - m + 1):
    j = 0
    while j < m:
        if p[j] != t[i + j]: 
            break
        j += 1

    if j == m:
        print(t[i:])
        break