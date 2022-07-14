
from itertools import combinations
from math import prod
from random import randrange
import sys
sys.stdin = open("./text/13926.txt")
input = sys.stdin.readline
dp = [i for i in range(10000)]
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

n = Int()
N = n
results = []
while n > 1:
    div = pollard_rho(n)
    results.append(div)
    n = n // div
    results = list(set(results))

_N = len(results)
cases = [[] for _ in range(_N + 1)]
for L in range(_N + 1):
    for subset in combinations(results, L):
        cases[len(subset)].append(subset)

result = N
cases = cases[1:]
for i in range(len(cases)):
    case = cases[i]
    for j in range(len(case)):
        num = N // prod(case[j])
        if i % 2 == 0:
            result -= num
        else:
            result += num
print(result)