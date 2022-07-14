import sys
sys.stdin = open('./text/1786.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def Str():return input().strip()
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]


S = Str()
P = Str()
M = len(P)
N = len(S)

def LPS(P):
    pi = [0] * M
    j = 0
    for i in range(1, M):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if P[i] == P[j]:
            pi[i] = j + 1
            j += 1
        else:
            pi[i] = 0
    return pi

def kmp(S, P):
    pi = LPS(P)
    j = 0
    result = []
    for i in range(N):
        while j > 0 and S[i] != P[j]:
            j = pi[j - 1]
        if S[i] == P[j]:
            if j == M - 1:
                result.append(i - (M - 1) + 1)
                j = pi[j]
            else:
                j += 1
    return result

result = kmp(S, P)               
print(len(result))
print(*result)