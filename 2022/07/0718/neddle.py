
from decimal import *
import sys
sys.stdin = open('./text/20176.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def Num(nums): 
    temp = [0] * (2 * P + 1)
    for num in nums:
        temp[num + P] = 1
    return temp

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

P = 30000
_ = Int()
A = Num(List())
_ = Int()
B = Num(List())
_ = Int()
C = Num(List())
AC = multiply(A, C)
print(sum([B[i] * AC[2 * i] for i in range(2 * P + 1)]))
