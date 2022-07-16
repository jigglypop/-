import sys
sys.stdin = open("./text/1305.txt")
input = sys.stdin.readline
def Int():return int(input().strip())
N = Int()
word = input() 

def LPS(pat):
    j = 0
    i = 1
    lps = [0] * N
    while i < N:
        if pat[i] == pat[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

print(N - LPS(word)[-1])