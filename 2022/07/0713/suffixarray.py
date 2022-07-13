import sys
sys.stdin = open('./text/9248.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]

S = input().strip()
N = len(S)
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
LCP[0] = 'x'
for sa in SA:
    print(sa + 1, end=" ")
print()
for lcp in LCP:
    print(lcp, end=" ")