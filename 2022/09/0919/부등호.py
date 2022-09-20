from copy import copy
from itertools import permutations
from pprint import pprint
import sys
sys.stdin = open('./text/2529.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(str, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
def A(v, Args):
    if isinstance(Args, int):
        return [copy(v) for _ in range(Args)]
    if len(Args) == 1:
        return [copy(v) for _ in range(Args[0])]
    return A([copy(v) for _ in range(Args.pop())], Args)

N = Int()
words = List()
calc = { '>': lambda x, y: x > y,  '<': lambda x, y: x < y }
count = 0
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
choices = []

def perm(k, choice, used):
    if k == N + 1:
        if calc[words[k - 2]](choice[k - 2], choice[k - 1]):
            choices.append("".join(map(str, choice))) 
            return
    if len(choice) >= 2:
        if not calc[words[k - 2]](choice[k - 2], choice[k - 1]):
            return 0
    for i in range(len(nums)):
        if used & (1 << i): continue
        perm(k + 1, choice + [nums[i]], used | (1 << i))

perm(0, [], 0)
choices.sort()
print(choices[-1])
print(choices[0])
