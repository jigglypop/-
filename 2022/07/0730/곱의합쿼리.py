from decimal import *
import sys
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def multiply(a, b, digit = 0):
    setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX))
    if digit == 0:
        digit = min(20, len(str(min(len(a), len(b)) * max(a) * max(b))))
    f = f'0{digit}d'
    a_dec = Decimal(''.join(format(x, f) for x in a))
    b_dec = Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) % P for i in range(0, total_digit, digit)]

P = 100003
N = Int()
board = List()

def go(s, e):
    if s > e: 
        return [1]
    if s == e: 
        return [board[s], 1]
    m = (s + e) // 2
    return multiply(go(s, m), go(m + 1, e))

result = go(0, N - 1)
for _ in range(Int()):
    print(result[N - Int()] % P)