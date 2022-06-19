import sys
sys.stdin = open("./text/4354.txt", "r")
input = sys.stdin.readline
words = []
while True:
    word = input().strip()
    if word == ".":
        break
    words.append(word)

def LPS(ptr):
    N = len(ptr)
    p = 0
    i = 1
    lps = [0] * N
    while i < N:
        if ptr[i] == ptr[p]:
            p += 1
            lps[i] = p
            i += 1
        else:
            if p != 0:
                p = lps[p - 1]
            else:
                p = 0
                i += 1
    return lps
    
for word in words:
    lps = LPS(word)
    l = len(word)
    p = l - lps[-1]
    if l % p == 0:
        print(l // p)
    else:
        print(1)