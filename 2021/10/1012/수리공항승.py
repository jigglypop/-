import sys
from pprint import pprint
from collections import deque
sys.stdin = open("./text/1449.txt", "r")
input = sys.stdin.readline
N, L = map(int, input().split())
nums = list(map(int, input().split()))
print(nums)