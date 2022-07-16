
import sys
sys.stdin = open('./text/4354.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()

while True:
    word = Str()
    if word == '.':break
    N = len(word)
    j = 0
    i = 1
    lps = [0] * N
    while i < N:
        if word[i] == word[j]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    D = N - lps[N - 1]
    if lps[N - 1] == 1:
        print(1)
    else:
        print(N // D)
