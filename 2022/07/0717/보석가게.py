
from collections import defaultdict
from math import cos, pi, sin
from decimal import *
import sys
sys.stdin = open('./text/13575.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000)]
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


N, K = Split()
nums = List()
A = [0] * (max(nums) + 1)
for i in range(len(nums)):
    A[nums[i]] += 1
dp = defaultdict(lambda: [])
def O(x): return list(map(lambda y: 1 if y else 0, x))
A = O(A)

def fft_pow(n):
  if n == 1: return A
  else:
    if dp[n]: 
        return dp[n]
    if n % 2 == 0: 
        dp[n] = O(multiply(fft_pow(n // 2), fft_pow(n // 2)))
        return dp[n]
    else: 
        dp[n] = O(multiply(fft_pow(n // 2), fft_pow(n // 2 + 1)))
        return dp[n]

result = fft_pow(K)
for i in range(len(result)):
  if result[i]: print(i, end=' ')