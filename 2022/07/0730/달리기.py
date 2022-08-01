import sys
from math import ceil, log2
sys.stdin = open('./text/2517.txt', 'r')
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline

N = Int()
nums = [Int() for _ in range(N)]
tree = [0] * (N + 1)
nums_sort = sorted(nums)
nums_obj = {}
for i in range(len(nums_sort)):
    num = nums_sort[i]
    nums_obj[num] = i + 1

def update(i):
    while i < len(tree):
        tree[i] += 1
        i += (i & -i)

def sum(i):
    s = 0
    while i > 0:
        s += tree[i]
        i -= (i & -i)
    return s

i = 2
for num in nums:
    _i = nums_obj[num]
    update(_i)
    print(i - sum(_i))
    i += 1