from collections import defaultdict
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/21921.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, X = Split()
nums = List()
if max(nums) == 0:
    print("SAD")
else:
    Max = sum(nums[:X])
    _Max = Max
    count = 1
    for i in range(X, N):
        Max -= nums[i - X]
        Max += nums[i]
        if Max > _Max:
            _Max = Max
            count = 1
        elif Max == _Max:
            count += 1
    print(_Max)
    print(count)