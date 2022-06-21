import random
import sys
sys.stdin = open("./text/5615.txt", "r")
input = sys.stdin.readline

def miller_rabin(n, b, s, t):
    x = pow(b, t, n) 
    if x == 1 or x == n-1:
        return 1
    else:
        for _ in range(s):
            if x == n-1:
                return 1
            x = pow(x,2,n)
        return 0

def is_prime(n):
    if n < 2 or not n & 1:
        return 0 
    if n == 2:
        return 1
    s = 0
    t = (n - 1)
    while t % 2 == 0:
        s += 1
        t >>= 1
    for _ in range(0, 250):
        b = random.randrange(2, n-1)
        test = miller_rabin(n, b, s, t)
        if test == 0:
            return 0
    return 1

result = 0
for _ in range(int(input())):
    if is_prime(2 * int(input()) + 1):
        result += 1
print(result)