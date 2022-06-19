import sys
sys.stdin = open("./text/1305.txt", "r")
input = sys.stdin.readline

N = int(input())
word = input() 

def LPS(pat):
    N = len(pat)
    p = 0
    i = 1
    lps = [0] * N
    while i < N:
        if pat[i] == pat[p]:
            p += 1
            lps[i] = p
            i += 1
        else:
            if p != 0:
                p = lps[p - 1]
            else:
                lps[i] = 0
                i += 1
    return lps
        
print(N - LPS(word)[-1])

