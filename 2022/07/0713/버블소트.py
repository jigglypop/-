from copy import copy
from pprint import pprint
import sys
sys.stdin = open('./text/1517.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())

N = Int()
nums = list(Split())
_nums = sorted(nums)
A = [i + 1 for i in range(N)]
B = []
maps = {}
for i in range(len(nums)):
    maps[nums[i]] = i + 1

for num in _nums:
    B.append(maps[num])
board = [0] * (N + 1)

def sum(i):
    res = 0
    while i > 0:
        res += board[i]
        i -= (i & -i)
    return res

def update(i, x):
    while i < len(board):
        board[i] += x
        i += (i & -i)

result = 0
for b in B:
    update(b, 1)
    result += sum(N) - sum(b)
print(result)