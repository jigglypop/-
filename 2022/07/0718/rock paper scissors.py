
from decimal import *
from itertools import zip_longest
import sys
sys.stdin = open('./text/14958.txt', 'r')
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

_, _ = Split()
a = Str()
b = Str()
s = len(b) - 1
R = multiply([1 if i == 'R' else 0 for i in a], [1 if i == 'P' else 0 for i in b][::-1])[s:] + [0]
S = multiply([1 if i == 'S' else 0 for i in a], [1 if i == 'R' else 0 for i in b][::-1])[s:] + [0]
P = multiply([1 if i == 'P' else 0 for i in a], [1 if i == 'S' else 0 for i in b][::-1])[s:] + [0]
print(max([sum(x) for x in zip_longest(R, S, P, fillvalue = 0)]))
