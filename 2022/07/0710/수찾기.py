import sys
from bisect import *
sys.stdin = open('./text/1920.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
M = int(input())
A = sorted(list(Split()))
N = int(input())
B = Split()
for b in B:
    print(0 if b in A else 1)
