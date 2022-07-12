from bisect import bisect_right
import sys
from math import *
sys.stdin = open('./text/1920.txt', 'r')
input = sys.stdin.readline
dp = [i for i in range(10000000)]
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]
N = Int()
A = set(Split())	
M = Int()
nums = list(Split())
for num in nums:				
    print(1) if num in A else print(0)	