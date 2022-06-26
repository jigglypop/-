import sys
sys.stdin = open("./text/9248.txt", "r")
input = sys.stdin.readline
C = input()
N = len(C)
SA = [i for i in range(N)]
_g = [0] * (N + 1) 
g = [ord(C[i]) for i in range(N)] + [-1]
_g[SA[0]] = 0
_g[N] = -1
t = 1
while t < N:
    SA.sort(key = lambda x :(g[x], g[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i-1], SA[i]
        if g[a] != g[b] or g[min(a + t, N)] != g[min(b + t, N)]:
            _g[b] = _g[a] + 1
        else:
            _g[b] = _g[a]
    t *= 2
    g = _g[:]

LCP = [0] * N
l = 0 
for i in range(N):
    if not g[i]: continue 
    j = SA[g[i] - 1]
    while i + l < N and j + l < N and C[i + l] == C[j + l]:
        l += 1
    LCP[g[i]] = l
    if l: l -= 1

LCP[0] = "x"
for sa in SA:
    print(sa + 1, end =" ")
print()
for lcp in LCP:
    print(lcp, end=" ")
