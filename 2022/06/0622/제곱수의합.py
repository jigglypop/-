from math import sqrt
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
    s = n - 1
    while not s % 2 and s:
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

def four_square(n):
    while n % 4 == 0:
        n //= 4
    return n % 8 == 7

def three_square(n):
    l = []
    while n > 1:
        d = pollard_rho(n)
        l.append(d)
        n //= d

    c = list(Counter(l).items())
    for i, n in c:
        if i % 4 == 3 and n % 2 == 1:
            return True
    return False

n = int(input())
if four_square(n):
    print(4)
elif three_square(n):
    print(3)
elif int(sqrt(n)) ** 2 != n:
    print(2)
else:
    print(1)
