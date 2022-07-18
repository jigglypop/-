
from decimal import *
from itertools import zip_longest
from pprint import pprint
import sys
sys.stdin = open('./text/5051.txt', 'r')
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

N = Int()
A = [0] * N
same = [0] * N
for i in range(1, N):
    A[i ** 2 % N] += 1
    same[2 * i ** 2 % N] += 1
C = multiply(A, A)
for i in range(N, len(C)):
    C[i % N] += C[i]
print(sum([A[i] * same[i] + A[i] * ((C[i] - same[i]) // 2) for i in range(N)]))