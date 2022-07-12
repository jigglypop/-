from itertools import permutations
import sys
sys.stdin = open("./text/15649.txt")
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

def gcd(a, b):
    while b > 0:a, b = b, a % b
    return a

N = Int()
A = Split()
M = Int()
B = Split()
a = b = 1
for i in A:
    a *= i
for j in B:
    b *= j
print(str(gcd(a, b))[-9:])