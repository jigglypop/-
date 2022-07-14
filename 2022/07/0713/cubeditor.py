import sys
sys.stdin = open('./text/1701.txt', 'r')
input = sys.stdin.readline
def Str():return input().strip()

def LPS(pat):
    pi = [0] * len(pat)
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]:
            j = pi[j - 1]
        if pat[i] == pat[j]:
            j += 1
            pi[i] = j
    return max(pi)

pat = Str()
result = 0
for i in range(len(pat)):
    result = max(result, LPS(pat[i:len(pat)]))
print(result)