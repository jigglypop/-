p = "CATTCCCTGCGCCGC"  
# m, j                                                                      # pattern
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

# 3. Brute-Force2
m, n = len(p), len(t)


i = 0
j = -1
next = [0] * (m+1)
next[0] = -1
while i < m :
    while j >= 0 and p[j] != p[i]:
        j = next[j]
    i, j = i + 1, j + 1
    next[i] = j
print(next)


i = j = 0
while i < n :
    while j >= 0 and 

