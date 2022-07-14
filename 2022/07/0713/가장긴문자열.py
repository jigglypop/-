import sys
sys.stdin = open('./text/3033.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
S = Str()
SA = [i for i in range(N)]
G = [ord(S[i]) for i in range(N)] + [-1]
_G = [0] * N + [-1]
t = 1
while t < N:
    SA.sort(key = lambda x : (G[x], G[min(x + t, N)]))
    for i in range(1, N):
        a, b = SA[i - 1], SA[i]
        if G[a] != G[b] or G[min(a + t, N)] != G[min(b + t, N)]:
            _G[b] = _G[a] + 1
        else:
            _G[b] = _G[a]
    t *= 2
    G = _G[:]

LCP = [0] * N
l = 0 
for i in range(N):
    if G[i] == 0: continue 
    j = SA[G[i] - 1]
    while i + l < N and j + l < N and S[i + l] == S[j + l]:
        l += 1
    LCP[G[i]] = l
    if l > 0: 
        l -= 1
print(max(LCP))