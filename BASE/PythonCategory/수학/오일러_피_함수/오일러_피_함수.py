import sys
from math import ceil
sys.stdin = open("11689.txt", "r")
input = sys.stdin.readline

N = int(input())


def phi(x):
    ans = x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            while x % i == 0:
                x /= i
            ans -= ans / i
    if x > 1:
        ans -= ans / x
    return ans


print(int(phi(N)))
