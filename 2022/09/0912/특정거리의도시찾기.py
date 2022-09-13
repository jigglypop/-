from collections import deque
from heapq import heappop, heappush
from pprint import pprint
import sys
sys.stdin = open('./text/18352.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N, M, K, X = Split()
tree = [[] for _ in range(N + 1)]
