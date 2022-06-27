import sys
sys.stdin = open("./text/9249.txt", "r")
input = sys.stdin.readline

words = [input(), input()]
word = "$".join(words)
N = len(word)
sa = [i for i in range(N)]
g = [ord(i) for i in word]
_g = [0] * N
def f(x): return g[x] if x < N else -1
t = 1
while t <= N:
    sa.sort(key = lambda x: (f(x), f(x + t)))
    p = 0
    _g[sa[0]] = 0
    for i in range(1, N):
        if f(sa[i - 1]) != f(sa[i]) or f(sa[i - 1] + t) != f(sa[i] + t):
            p += 1
        _g[sa[i]] = p
    g = _g[:]
    t *= 2


# Get LCP Array
LCP = [0] * N
l = 0 
for i in range(N):
    k = g[i]
    if k==0: # 처음은 들어가지 않는다.
        continue 
    p = sa[k-1]

    while i + l < N and p + l < N and s[i+l] == s[p+l]:
        l += 1
    LCP[k] = l
    if l:l-=1


# 나누어진 영역에서의 최대값 구하기
m =(0,0) # length, start_index
for i, j in enumerate(LCP):
    if 0 <= sa[i-1] + j - 1<len(A) and len(A) < sa[i] + j-1 <len(s):
        m = max(m,(j,i))
    if 0 <= sa[i] + j - 1<len(A) and len(A) < sa[i-1] + j-1 <len(s):
        m = max(m,(j,i))
    
length, start = m
print(length)
print(s[sa[start]: sa[start] + length])