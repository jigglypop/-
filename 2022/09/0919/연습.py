from collections import deque
from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/17412.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)

