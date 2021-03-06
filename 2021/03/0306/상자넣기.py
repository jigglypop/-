import sys
from pprint import pprint
sys.stdin = open('1965.txt', 'r')
input = sys.stdin.readline
N = int(input())
boxs = list(map(int, input().split()))
size = [0] * 1001
for b in boxs:
    size[b] = max(size[:b]) + 1
print(max(size))
