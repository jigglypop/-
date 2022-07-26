from decimal import *
import sys
sys.stdin = open('./text/13055.txt', 'r')
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

word = input()
N = len(word)
A = [0] * N
B = [0] * N
for i, w in enumerate(word):
    if w == 'A':
        A[i] = 1
    else:
        B[N-1-i] = 1
C = multiply(A, B)
print(*C[N:2 * N], sep = "\n")