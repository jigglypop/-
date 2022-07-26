from decimal import *
import sys
sys.stdin = open('./text/14756.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def multiply(a, b, digit = 0):
    setcontext(Context(prec = MAX_PREC, Emax = MAX_EMAX))
    if digit == 0:
        digit = 20
    f = f'0{digit}d'
    a_dec = Decimal(''.join(format(x, f) for x in a))
    b_dec = Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]

N, L, M, W = Split()
S = []
T = []
for _ in range(M):
    S += [List()]
for _ in range(M):
    T += [List()]
result = [0] * (N - L + 1)
for i in range(M):
    temp = multiply(S[i], T[i][::-1])
    for j in range(L - 1, N):
        result[j - L + 1] += temp[j]
		
answer = 0
for i in result:
	if i > W: answer += 1
print(answer)