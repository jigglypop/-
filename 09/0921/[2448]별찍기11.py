import math
import sys
from pprint import pprint
sys.stdin = open('2448.txt', 'r')


def make_stars(shift, s):
    for i in range(len(s)):
        s.append(s[i]+s[i])
        s[i] = ' ' * shift + s[i] + ' ' * shift


def solution():
    s = ['  *   ', ' * *  ', '***** ']

    num = int(input())
    k = int(math.log(num / 3, 2))

    for i in range(k):
        make_stars(2 ** i * 3, s)

    for i in range(len(s)):
        print(s[i])


solution()
