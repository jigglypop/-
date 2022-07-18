
from decimal import *
import sys
sys.stdin = open('./text/17134.txt', 'r')
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

MAX = 1000001
prime = [1] * MAX
prime[0] = prime[1] = 0
M = int(MAX ** 0.5)
for i in range(2, M + 1):
    if prime[i]:   
        for j in range(i + i, MAX, i): 
            prime[j] = 0
semi_prime = [0] * MAX
for i in range(MAX//2):
  if prime[i]: semi_prime[2*i] = 1
prime[2] = 0

C = multiply(prime, semi_prime)
for _ in range(Int()):
    print(C[Int()])
