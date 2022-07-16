
from collections import Counter
from math import sqrt
from random import randrange
import sys
sys.stdin = open("./text/17633.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def millor_rabin(n):
    for p in [2, 3, 5, 7, 11, 13, 17]:
        if p == n:
            return True
        r = 0
        d = n - 1
        while not (d % 2):
            r += 1
            d //= 2
        x = pow(p, d, n)
        flag = False
        for i in range(r):
            if (x == 1 and i == 0) or x == n - 1:
                flag = True
                break
            x = pow(x, 2, n)
        if not flag: return False
    return True

def pollard_rho(n):
    if millor_rabin(n):
        return n
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    x = randrange(2, n)
    y = x
    c = randrange(1, n)
    d = 1
    while d == 1:
        calc = lambda x : ((x ** 2 % n) + c + n) % n
        x = calc(x)
        y = calc(y)
        y = calc(y)
        d = gcd(abs(x - y), n)
        if d == n: return pollard_rho(n)
    return pollard_rho(d)

def calc():
    N = Int()
    n = N
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        print(4)
        return
    results = []
    n = N
    while n > 1:
        div = pollard_rho(n)
        results.append(div)
        n //= div
    
    c = list(Counter(results).items())
    for i, n in c:
        if i % 4 == 3 and n % 2 == 1:
            print(3)
            return
    n = N
    if int(sqrt(n)) ** 2 != n:
        print(2)
        return 
    else:
        print(1)
        return 

calc()