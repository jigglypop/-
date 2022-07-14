
import sys
import random
sys.stdin = open('./text/4149.txt', 'r')
input = sys.stdin.readline
def Int():return int(input().strip())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def millor_rabin(a, p):
    r = 0
    d = p - 1
    while not (d % 2):
        r += 1
        d //= 2
    x = pow(a, d, p)
    for i in range(r):
        if (x == 1 and i == 0) or x == p - 1: 
            return True
        x = pow(x, 2, p)
    return False

# def pollard_rho(n):
#     if millor_rabin(n):
#         return n
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return 2
#     x = random.randrange(2, n)
#     y = x
#     c = random.randrange(1, n)
#     d = 1
#     while d == 1:
#         x = ((x ** 2 % n) + c + n) % n
#         y = ((y ** 2 % n) + c + n) % n
#         y = ((y ** 2 % n) + c + n) % n
#         d = gcd(abs(x - y), n)
#         if d == n:
#             return pollard_rho(n)
#     if millor_rabin(d):
#         return d
#     else:
#         return pollard_rho(d)

A = 12
flag = True
for p in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
    print(millor_rabin(A, p))
    if not millor_rabin(A, p):
        flag = False
        break
print(flag)
# results = []
# while N > 1:
#     div = pollard_rho(N)
#     results.append(div)
#     N = N // div
# results.sort()
# for result in results:
#     print(result)