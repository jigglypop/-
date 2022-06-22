import collections
import sys
import random
from collections import *
sys.stdin = open("./text/10854.txt", "r")
input = sys.stdin.readline

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def millor_rabin(n):
    prime = [2,7,61]
    if n in prime:
        return True
    if n % 2 ==0 or n == 1:
        return False
    r = 0
    s = n-1
    while not s%2 and s:
        r += 1
        s = s//2

    def calc(a):
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
        
    for a in prime:
        if calc(a):
            return False
    return True

def pollard_rho(n):
    if millor_rabin(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = random.randrange(2, n)
    y = x
    c = random.randrange(1, n)
    d = 1
    while d == 1:
        x = ((x ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        y = ((y ** 2 % n) + c + n) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    if millor_rabin(d):
        return d
    else:
        return pollard_rho(d)
 
n = int(input())
results = []
while n > 1:
    divisor = pollard_rho(n)
    results.append(divisor)
    n = n // divisor
 
result_map = Counter(results)
result = 1
for v in result_map.values():
    result *= (v + 1)
print(result)