from math import gcd
from functools import reduce
from operator import mul
import sys
sys.stdin = open("2824.txt", "r")
input = sys.stdin.readline
input()
x = reduce(mul, map(int, input().split()))
input()
print(str(gcd(x, reduce(mul, map(int, input().split()))))[-9:])
